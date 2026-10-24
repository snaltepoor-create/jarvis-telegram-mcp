from __future__ import annotations

import json
import os
from contextlib import asynccontextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import AsyncIterator

from telethon import TelegramClient


class TelegramSetupError(RuntimeError):
    pass


@dataclass(frozen=True)
class TelegramConfig:
    api_id: int
    api_hash: str
    session_path: Path


def data_dir() -> Path:
    override = os.getenv("JARVIS_TELEGRAM_HOME")
    if override:
        return Path(override).expanduser().resolve()

    local_app_data = os.getenv("LOCALAPPDATA")
    if local_app_data:
        return Path(local_app_data) / "JarvisTelegram"
    return Path.home() / ".local" / "share" / "JarvisTelegram"


def config_path() -> Path:
    return data_dir() / "config.json"


def default_session_path() -> Path:
    return data_dir() / "telegram-session"


def load_config() -> TelegramConfig:
    path = config_path()
    stored: dict[str, object] = {}
    if path.exists():
        try:
            stored = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise TelegramSetupError(f"Не удалось прочитать настройки {path}: {exc}") from exc
        if not isinstance(stored, dict):
            raise TelegramSetupError(f"Файл настроек должен содержать JSON-объект: {path}")

    raw_api_id = os.getenv("TG_API_ID") or stored.get("api_id")
    api_hash = os.getenv("TG_API_HASH") or stored.get("api_hash")
    raw_session_path = os.getenv("TG_SESSION_PATH") or stored.get("session_path")

    if not raw_api_id or not api_hash:
        raise TelegramSetupError(
            "Telegram не настроен. Запусти login.py из каталога плагина и введи API ID/API hash с my.telegram.org."
        )

    try:
        api_id = int(raw_api_id)
    except (TypeError, ValueError) as exc:
        raise TelegramSetupError("TG_API_ID должен быть целым числом.") from exc

    if api_id <= 0 or not isinstance(api_hash, str) or not api_hash.strip():
        raise TelegramSetupError("В настройках Telegram указан некорректный API ID или API hash.")

    session_path = Path(str(raw_session_path)).expanduser() if raw_session_path else default_session_path()
    return TelegramConfig(api_id=api_id, api_hash=api_hash.strip(), session_path=session_path)


def save_config(api_id: int, api_hash: str, session_path: Path | None = None) -> Path:
    if api_id <= 0 or not api_hash.strip():
        raise TelegramSetupError("Нужны корректные Telegram API ID и API hash.")

    directory = data_dir()
    directory.mkdir(parents=True, exist_ok=True)
    config_file = directory / "config.json"
    final_session_path = session_path or default_session_path()
    payload = {
        "api_id": api_id,
        "api_hash": api_hash.strip(),
        "session_path": str(final_session_path),
    }
    temporary = config_file.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    os.replace(temporary, config_file)
    return config_file


@asynccontextmanager
async def connected_client(require_authorized: bool = True) -> AsyncIterator[tuple[TelegramClient, bool]]:
    config = load_config()
    config.session_path.parent.mkdir(parents=True, exist_ok=True)
    client = TelegramClient(str(config.session_path), config.api_id, config.api_hash)
    try:
        await client.connect()
        authorized = await client.is_user_authorized()
        if require_authorized and not authorized:
            raise TelegramSetupError("Нет авторизованной Telegram-сессии. Сначала запусти login.py.")
        yield client, authorized
    finally:
        if client.is_connected():
            await client.disconnect()
