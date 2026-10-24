from __future__ import annotations

import asyncio
import getpass
import os

from telethon import TelegramClient

from telegram_service import default_session_path, save_config


async def main() -> None:
    raw_api_id = os.getenv("TG_API_ID") or input("Telegram API ID: ").strip()
    api_hash = os.getenv("TG_API_HASH") or getpass.getpass("Telegram API hash: ").strip()
    try:
        api_id = int(raw_api_id)
    except ValueError as exc:
        raise SystemExit("API ID должен быть целым числом.") from exc

    session_path = default_session_path()
    session_path.parent.mkdir(parents=True, exist_ok=True)
    client = TelegramClient(str(session_path), api_id, api_hash)
    try:
        await client.start()
        if not await client.is_user_authorized():
            raise SystemExit("Telegram не подтвердил авторизацию.")
        account = await client.get_me()
        config_file = save_config(api_id, api_hash, session_path)
        name = " ".join(part for part in [account.first_name, account.last_name] if part)
        print(f"Авторизовано: {name or account.id} (@{account.username or 'без username'}).")
        print(f"Настройки сохранены: {config_file}")
        print(f"Сессия сохранена: {session_path}.session")
    finally:
        if client.is_connected():
            await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
