# AI Agents

AI agents are software systems that perceive their environment, make decisions, and take actions to achieve a goal — often autonomously and over multiple steps. They can use tools, call APIs, write and run code, and chain reasoning steps together. Modern AI agents are typically powered by large language models and can operate with minimal human intervention. 
 
For the ElectroAI Hackathon, we will be using one or more of the following AI Agents: Claude Code, Codex and Gemini CLI. If you are subscribing to Anthropic (to use claude.ai), or OpenAI (to use chatgpt.com), you have by default a quota to use their respective AI Agent. We will default to Gemini CLI, which has on occasion free one-year student offers (if you have signed up at some point, you are all set) and also a one month free trial current offer (as of end of March). It is essential that you have at least one AI Agent running, to work on your hackathon project. 
 
## Installing Claude

### macOS

1. Install [Homebrew](https://brew.sh) if not already installed.
2. Run: `brew install node`
3. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
4. Authenticate: `claude` (follow the browser login prompt)

### Windows

1. Install [Node.js](https://nodejs.org) (LTS recommended).
2. Open PowerShell or Command Prompt.
3. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
4. Authenticate: `claude` (follow the browser login prompt)

## Installing Codex

### macOS

1. Install [Homebrew](https://brew.sh) if not already installed.
2. Run: `brew install node`
3. Install Codex: `npm install -g @openai/codex`
4. Sign in: `codex --login`

### Windows

1. Install [Node.js](https://nodejs.org) (LTS recommended).
2. Open PowerShell or use WSL if needed.
3. Install Codex: `npm install -g @openai/codex`
4. Sign in: `codex --login`

Note: On Windows, you may need to run the terminal as Administrator.

## Installing Gemini CLI

### macOS

1. Install [Homebrew](https://brew.sh) if not already installed.
2. Run: `brew install gemini-cli` or `npm install -g @google/gemini-cli`
3. Authenticate: `gemini`

### Windows

1. Install [Node.js](https://nodejs.org) (LTS recommended).
2. Run: `npm install -g @google/gemini-cli`
3. Authenticate: `gemini`

## Terminal Cheat Sheet

### macOS

- Show current folder: `pwd`
- List files: `ls`
- Change folder: `cd folder-name`
- Go up one folder: `cd ..`
- Create folder: `mkdir new-folder`
- Copy file: `cp old.txt new.txt`
- Move or rename: `mv old.txt new.txt`
- Delete file: `rm file.txt`
- Clear screen: `clear`

### Windows

- Show current folder: `cd`
- List files: `dir`
- Change folder: `cd folder-name`
- Go up one folder: `cd ..`
- Create folder: `mkdir new-folder`
- Copy file: `copy old.txt new.txt`
- Move or rename: `move old.txt new.txt`
- Delete file: `del file.txt`
- Clear screen: `cls`
