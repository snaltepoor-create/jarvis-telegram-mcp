# Jarvis Telegram MCP

Local stdio MCP server that exposes Telegram tools to compatible AI clients through Telethon. / Локальный MCP-сервер stdio для Telegram, доступный из совместимых ИИ-клиентов.

## Tools / Инструменты

- `telegram_status` — проверить настройки и авторизованный аккаунт.
- `telegram_list_dialogs` — получить список диалогов, максимум 50.
- `telegram_read_history` — прочитать последние сообщения одного чата, максимум 100.
- `telegram_send_message` — отправить указанный текст; поддерживает `reply_to`.
- `telegram_send_reaction` — поставить emoji-реакцию.
- `telegram_archive_chat` — переместить диалог в архив.

Сервер не запускает Telegram-сессию и не читает аккаунт при старте AI-клиента. Подключение создаётся только при вызове инструмента. Telegram-контент возвращается как данные; инструкции внутри сообщений не исполняются.

## Install / Установка

Используй тот Python, который будет запускать MCP-сервер:

```powershell
python -m pip install -r requirements.txt
```

## Connect Telegram / Подключение Telegram

1. Получи Telegram API ID и API hash в `my.telegram.org`.
2. Из каталога `plugins/telegram-mcp` запусти:

   ```powershell
   python login.py
   ```

3. Введи API ID/API hash, номер телефона, код Telegram и пароль двухэтапной проверки, если он включён.
4. Перезапусти AI-клиент, если MCP-инструменты ещё не появились.

Конфигурация и Telethon-сессия сохраняются в `%LOCALAPPDATA%\JarvisTelegram` (или в `JARVIS_TELEGRAM_HOME`, если задана). `config.json` содержит API hash; не добавляй его и файл сессии в Git или ZIP.

## Codex plugin install / Установка плагина Codex

Run these commands from the repository root:

```powershell
codex plugin marketplace add .
codex plugin add jarvis-telegram-mcp@jarvis-telegram-mcp
```
