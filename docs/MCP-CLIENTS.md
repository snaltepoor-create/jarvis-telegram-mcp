# MCP client setup

The server uses MCP over local standard input/output (`stdio`). Install dependencies and complete Telegram login before connecting a client:

```powershell
python -m pip install -r plugins/telegram-mcp/requirements.txt
python plugins/telegram-mcp/login.py
```

Replace `C:/absolute/path/to/repository` in the examples with the full path to this checkout. Use the Python executable that has the listed dependencies installed.

## Codex

Install the bundled plugin from the repository root:

```powershell
codex plugin marketplace add .
codex plugin add jarvis-telegram-mcp@jarvis-telegram-mcp
```

Or add the MCP server directly:

```powershell
codex mcp add jarvis-telegram-mcp -- python "C:\absolute\path\to\repository\plugins\telegram-mcp\server.py"
```

## Cursor

Add the following server under `mcpServers` in `.cursor/mcp.json` or the global `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "jarvis-telegram-mcp": {
      "command": "python",
      "args": ["C:/absolute/path/to/repository/plugins/telegram-mcp/server.py"]
    }
  }
}
```

## VS Code with GitHub Copilot

Add this entry to `.vscode/mcp.json`:

```json
{
  "servers": {
    "jarvis-telegram-mcp": {
      "type": "stdio",
      "command": "python",
      "args": ["${workspaceFolder}/plugins/telegram-mcp/server.py"]
    }
  }
}
```

## Claude Code

Run this command, replacing the path with the absolute path to `server.py`:

```powershell
claude mcp add --scope user --transport stdio jarvis-telegram-mcp -- python "C:\absolute\path\to\repository\plugins\telegram-mcp\server.py"
```

Check the connection with `/mcp` in Claude Code.

## Other MCP clients

For a client that accepts a local stdio command, use this server entry and adapt the surrounding JSON shape to that client's config schema:

```json
{
  "command": "python",
  "args": ["/absolute/path/to/repository/plugins/telegram-mcp/server.py"]
}
```

MCP standardizes the server protocol; it does not make every AI application an MCP client. ChatGPT web and other remote-only clients cannot start a process on your computer. They need a hosted HTTP transport or a supported secure tunnel, neither of which is included here. ChatGPT's current custom MCP setup expects a reachable endpoint; local MCP apps are available only in its desktop flow. This repository does not bundle a remote transport or a ChatGPT desktop package.

## Official client references

- [Codex MCP setup](https://developers.openai.com/codex/mcp)
- [Claude Code MCP setup](https://code.claude.com/docs/en/mcp)
- [Cursor MCP setup](https://docs.cursor.com/context/model-context-protocol)
- [VS Code MCP configuration](https://code.visualstudio.com/docs/agents/reference/mcp-configuration)
- [ChatGPT MCP connectors](https://help.openai.com/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt)
