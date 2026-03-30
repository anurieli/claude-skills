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

There's one manual step, then Claude handles the rest.

### Step 1: Register the marketplace (you do this once)

Open `~/.claude/settings.json` and add `anurieli-skills` to your `extraKnownMarketplaces`. If the file doesn't exist or is empty, create it with this content:

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

If the file already has content, just add the `anurieli-skills` entry inside the existing `extraKnownMarketplaces` block (create the block if it doesn't exist).

### Step 2: Install the plugin (tell Claude to do it)

Open Claude Code and paste this:

```
Install the claude-skills plugin from the anurieli-skills marketplace. Run: /plugin install claude-skills@anurieli-skills
```

That's it. All skills and commands are now available.

### Updating

When new skills are added to this repo, tell Claude:

```
Reload plugins to pull the latest skills. Run: /reload-plugins
```

---

## Why the manual step?

`settings.json` controls which marketplaces Claude Code trusts. Editing it requires you (the human) to opt in — Claude can't modify its own settings file to add a new marketplace. Once the marketplace is registered, Claude can install and update plugins from it on its own.

---

## Legacy Install (Script)

If you prefer symlinks over the plugin system:

```bash
git clone https://github.com/anurieli/claude-skills.git ~/claude-skills
cd ~/claude-skills && ./install.sh
```

Update: `cd ~/claude-skills && git pull && ./install.sh`
Uninstall: `cd ~/claude-skills && ./uninstall.sh`
