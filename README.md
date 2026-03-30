# Claude Code Skills

Shared Claude Code skills and commands for use across machines and Claude Code instances.

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

---

## Install via Plugin (Recommended)

The plugin system is the easiest way to install on any machine. Two commands:

```
/plugin marketplace add anurieli/claude-skills
/plugin install claude-skills@anurieli-skills
```

### Auto-Discovery (Optional)

To pre-register the marketplace so you only need the install step, add this to `~/.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "anurieli-skills": {
      "source": {
        "source": "github",
        "repo": "anurieli/claude-skills"
      }
    }
  }
}
```

Then just run:

```
/plugin install claude-skills@anurieli-skills
```

### Updating

After new skills are pushed to the repo:

```
/reload-plugins
```

---

## Install via Script (Legacy)

Clone the repo and symlink everything into `~/.claude/`:

```bash
git clone https://github.com/anurieli/claude-skills.git ~/claude-skills
cd ~/claude-skills
./install.sh
```

### Update

```bash
cd ~/claude-skills
git pull
./install.sh
```

### Uninstall

```bash
cd ~/claude-skills
./uninstall.sh
```
