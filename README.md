# Jarvis Telegram MCP

**A local Telegram MCP server for AI assistants, powered by Telethon.** Connect it to MCP-compatible clients that can start local `stdio` servers, including Codex, Claude Code, Cursor, and VS Code with GitHub Copilot.

**Локальный MCP-сервер Telegram для ИИ-ассистентов на базе Telethon.** Подключается к совместимым MCP-клиентам с поддержкой локального `stdio`, включая Codex, Claude Code, Cursor и VS Code с GitHub Copilot.

## Features / Возможности

- Check the Telegram connection and authorized account.
- List up to 50 dialogs and read up to 100 recent messages from a selected chat.
- Send a requested message, react to a specified message, or archive a selected chat.
- No separate LLM API key: the AI client calls this local MCP server.
- No background listener, autonomous replies, deleted-message recovery, disappearing-media capture, desktop screenshots, or REST service.

Tools that change Telegram state run only after an explicit request. Telegram messages are treated as external data, not as instructions to the assistant.

## Requirements

- An AI client with local MCP over `stdio`
- Python 3.10+
- Telegram API ID and API hash from [my.telegram.org](https://my.telegram.org)

## Install

From the repository root, install the server dependencies:

```powershell
python -m pip install -r plugins/telegram-mcp/requirements.txt
```

Configure the Telegram account once:

```powershell
cd plugins/telegram-mcp
python login.py
```

Enter the API ID, API hash, phone number, Telegram login code, and two-step verification password if enabled. The session and config are stored outside the repository in `%LOCALAPPDATA%\JarvisTelegram` on Windows or `~/.local/share/JarvisTelegram` on Linux/macOS. Set `JARVIS_TELEGRAM_HOME` to use another directory. Never commit `config.json` or `*.session` files.

## Connect an AI client

The MCP server is host-neutral, but each client has its own configuration file and installation flow. See [`docs/MCP-CLIENTS.md`](docs/MCP-CLIENTS.md) for Codex, Cursor, VS Code/Copilot, and Claude Code examples.

This release uses local `stdio`. A client that accepts only a remote MCP URL needs a separately deployed HTTP transport. The server is not exposed to the public internet by this package.

## Tools

| Tool | Purpose |
| --- | --- |
| `telegram_status` | Check setup and the authenticated account |
| `telegram_list_dialogs` | List up to 50 dialogs |
| `telegram_read_history` | Read up to 100 recent messages from one chat |
| `telegram_send_message` | Send the exact requested text to a specified chat |
| `telegram_send_reaction` | React to a specified message |
| `telegram_archive_chat` | Move a specified dialog to the archive |

## Лицензия

Репозиторий распространяется по MIT License. Полный текст — в [`LICENSE`](LICENSE).
