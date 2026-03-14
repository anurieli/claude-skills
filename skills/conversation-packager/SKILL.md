---
name: conversation-packager
description: Packages the current or preceding Manus conversation into a structured Notion page — summarizing it, extracting action items, and capturing key decisions. Use this skill when the user says things like "package this conversation", "save this to Notion", "wrap this up", "capture this session", or "actionize this". The conversation to package is always the live chat history in context — no file or paste needed.
---

# Conversation Packager

This skill captures the current Manus conversation, extracts structured information using an LLM, and saves a formatted page to the **Conversation Packages** Notion database in the user's CutTheEdge HQ workspace.

## Notion Zone

- **Zone page:** https://www.notion.so/3135c17ca45b8192aa94ef97c7d524b7
- **Location in workspace:** HOME > 🗂️ Conversation Packages
- **Database data source ID:** `ee89e202-82a4-45bf-918a-6058df9a240d`

## Workflow

1. **Reconstruct the conversation** — From the current context, compile the full conversation history into a plain-text transcript. Format it as:
   ```
   User: [message]
   Manus: [response]
   User: [message]
   ...
   ```
   Include all meaningful exchanges. Omit tool call internals and system noise — keep only the human-readable dialogue.

2. **Save the transcript to a temp file** — Write the compiled transcript to `/tmp/conversation_transcript.txt`.

3. **Run the packager script:**
   ```bash
   python3 /home/ubuntu/skills/conversation-packager/scripts/package_conversation.py /tmp/conversation_transcript.txt
   ```

4. **Report the result** — Share the Notion page URL with the user and confirm it was saved.

## Output Format

Each Notion page contains:

| Field        | Description                                        |
|--------------|----------------------------------------------------|
| Title        | Short descriptive title (e.g. "Session: Skill Build") |
| Date         | Date of the conversation (YYYY-MM-DD)              |
| Topic        | Main topic or project discussed                    |
| Participants | Comma-separated (e.g. "User, Manus")               |
| Summary      | 2–4 sentence summary of the discussion             |
| Action Items | Count of action items (checklist in page body)     |
| Decisions    | Count of key decisions (listed in page body)       |

The page body includes:
- **Summary** section (prose)
- **Action Items** section (markdown checklist with owner and due date)
- **Key Decisions** section (bulleted list)

## Notes

- The conversation being packaged is always the **current session's chat history** — not an attached file or pasted text, unless the user explicitly provides one.
- If the user says "package the last conversation" or "save what we just discussed", treat the entire preceding dialogue in context as the source.
- Participants default to "User, Manus" for AI sessions unless real names are mentioned.
- If no action items or decisions exist, the script handles that gracefully.

## References

- See `references/notion_schema.md` for the full database schema.
- See `templates/notion_page_template.md` for the page content template.
