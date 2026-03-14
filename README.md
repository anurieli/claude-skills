# Claude Code Skills

Shared Claude Code skills and commands. Clone on any machine and run the install script to symlink everything into `~/.claude/`.

## Skills

| Skill | Description |
|-------|-------------|
| `call-to-linear` | Sync Fireflies call notes into Linear tasks |
| `conversation-packager` | Package conversations into Notion pages |
| `internal-comms` | Write internal communications (status reports, updates, FAQs) |
| `linear-project-generator` | Generate Linear project hierarchies from project docs |
| `schedule` | Create scheduled/recurring tasks |
| `skill-creator` | Create, modify, and evaluate skills |

## Commands

| Command | Description |
|---------|-------------|
| `/design-system-creation-prompt` | Create design systems and style guides |
| `/find-edge-cases` | Find production edge cases in frontend code |
| `/fix` | Run dev server and fix errors in a loop |
| `/teach` | Post-session technical deep dive |
| `/up-next` | Get next task from task manager |
| `/update-claude-md` | Update CLAUDE.md |
| `/update-prd` | Update PRD from README |
| `/upload-article` | Upload blog articles |

## Install

```bash
git clone https://github.com/anurieli/claude-skills.git ~/claude-skills
cd ~/claude-skills
./install.sh
```

## Update

```bash
cd ~/claude-skills
git pull
./install.sh
```

## Uninstall

```bash
cd ~/claude-skills
./uninstall.sh
```
