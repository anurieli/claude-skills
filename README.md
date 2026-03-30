# Claude Code Skills

Shared Claude Code skills and commands for use across machines and Claude Code instances.

## What's Included

### Skills

| Skill | Description |
|-------|-------------|
| `call-to-linear` | Sync Fireflies call notes into Linear tasks |
| `conversation-packager` | Package conversations into Notion pages |
| `internal-comms` | Write internal communications (status reports, updates, FAQs) |
| `linear-project-generator` | Generate Linear project hierarchies from project docs |
| `schedule` | Create scheduled/recurring tasks |
| `skill-creator` | Create, modify, and evaluate skills |

### Commands

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

## Setup

Open Claude Code and paste this:

```
Set up the anurieli/claude-skills plugin marketplace. Do the following:

1. Read ~/.claude/settings.json (create it if it doesn't exist)
2. Add this entry to the "extraKnownMarketplaces" object (create the object if it doesn't exist):

   "anurieli-skills": {
     "source": {
       "source": "github",
       "repo": "anurieli/claude-skills"
     }
   }

3. Write the updated settings.json
4. Run: /plugin install claude-skills@anurieli-skills
```

That's it. Claude does everything.

### Updating

When new skills are pushed to this repo, tell Claude:

```
Reload plugins to pull the latest skills. Run: /reload-plugins
```

---

## Legacy Install (Script)

If you prefer symlinks over the plugin system:

```bash
git clone https://github.com/anurieli/claude-skills.git ~/claude-skills
cd ~/claude-skills && ./install.sh
```

Update: `cd ~/claude-skills && git pull && ./install.sh`
Uninstall: `cd ~/claude-skills && ./uninstall.sh`
