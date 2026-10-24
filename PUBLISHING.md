# Публикация на GitHub

Локальный репозиторий уже создан на ветке `main`, файлы подготовлены к первому коммиту. GitHub CLI должен быть авторизован под аккаунтом владельца репозитория. В текущем окружении в Git пока не заданы `user.name` и `user.email`.

Рекомендуемое GitHub-имя — `jarvis-telegram-mcp`: оно сохраняет бренд и содержит поисковые слова Telegram и MCP. Описание репозитория: `Local Telegram MCP server for AI assistants, powered by Telethon.` Темы: `telegram`, `mcp`, `mcp-server`, `ai-assistant`, `telethon`, `telegram-api`, `python`, `codex`, `claude`, `cursor`, `vscode`.

После завершения `gh auth login` открой PowerShell в корне этого каталога и задай авторство коммита своими данными:

```powershell
git config user.name "Ваше имя или GitHub username"
git config user.email "Email, подтверждённый GitHub"
git commit -m "Release Jarvis Telegram MCP server"
gh repo create jarvis-telegram-mcp --public --description "Local Telegram MCP server for AI assistants, powered by Telethon." --source . --remote origin --push
gh repo edit --add-topic telegram --add-topic mcp --add-topic mcp-server --add-topic ai-assistant --add-topic telethon --add-topic telegram-api --add-topic python --add-topic codex --add-topic claude --add-topic cursor --add-topic vscode
```

Репозиторий публикуется публично под MIT. MCP-сервер локальный, transport `stdio`; установка в каждом ИИ-клиенте настраивается отдельно. Для ChatGPT Web и других хостов, принимающих только удалённый MCP, нужен HTTP transport и отдельное размещение сервера.
