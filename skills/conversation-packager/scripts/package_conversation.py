#!/usr/bin/env python3
"""
Conversation Packager Script
Analyzes a conversation transcript, extracts structured information,
and creates a Notion page in the Conversation Packages database.

Usage:
    python3 package_conversation.py <transcript_text_or_file_path>

The input can be:
- A path to a text file containing the conversation transcript
- A raw string of conversation text passed directly
"""

import json
import subprocess
import sys
import os
from openai import OpenAI

# The Notion data source ID for the Conversation Packages database
# Located inside: HOME > 🗂️ Conversation Packages > Conversation Packages (database)
DATABASE_ID = "ee89e202-82a4-45bf-918a-6058df9a240d"
# The Notion zone page URL
NOTION_ZONE_URL = "https://www.notion.so/3135c17ca45b8192aa94ef97c7d524b7"

client = OpenAI()


def analyze_conversation(transcript: str) -> dict:
    """Use an LLM to analyze a conversation transcript and extract structured information."""

    prompt = f"""You are an expert at analyzing conversations and extracting structured information.

Given the following conversation transcript (which may be a Manus AI session, meeting, chat, or any discussion), extract:
1. A concise summary (2-4 sentences) of what was discussed and decided
2. A list of action items (each with: task, owner, due date if mentioned)
3. A list of key decisions made
4. The main topic/project
5. The participants (infer from context — e.g. "User" and "Manus" for an AI session, or named people if mentioned)
6. The date of the conversation (if mentioned, otherwise use today's date in YYYY-MM-DD format)

Return your response as a JSON object with these exact keys:
- "title": A short descriptive title for this conversation (e.g., "Session: Building Conversation Packager Skill")
- "date": The date in YYYY-MM-DD format
- "topic": The main topic or project
- "participants": Comma-separated list of participant names
- "summary": A concise summary of the conversation
- "action_items": A markdown-formatted list of action items (use "- [ ] Task (Owner, Due: date)" format, or "- [ ] Task (Owner)" if no due date). If none, write "No action items identified."
- "key_decisions": A markdown-formatted list of key decisions (use "- Decision" format). If none, write "No key decisions identified."
- "action_item_count": Integer count of action items (0 if none)
- "decision_count": Integer count of decisions (0 if none)

CONVERSATION TRANSCRIPT:
{transcript}

Return ONLY the JSON object, no other text."""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)


def create_notion_page(data: dict) -> dict:
    """Create a Notion page in the Conversation Packages database."""

    content = f"""## Summary

{data['summary']}

## Action Items

{data['action_items']}

## Key Decisions

{data['key_decisions']}
"""

    pages = [
        {
            "properties": {
                "Title": data["title"],
                "date:Date:start": data["date"],
                "date:Date:is_datetime": 0,
                "Topic": data["topic"],
                "Summary": data["summary"],
                "Action Items": data["action_item_count"],
                "Decisions": data["decision_count"],
                "Participants": data["participants"]
            },
            "content": content
        }
    ]

    parent = {"data_source_id": DATABASE_ID}

    input_json = {
        "parent": parent,
        "pages": pages
    }

    cmd = [
        "manus-mcp-cli", "tool", "call", "notion-create-pages",
        "--server", "notion",
        "--input", json.dumps(input_json)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Failed to create Notion page: {result.stderr}")

    output = result.stdout
    try:
        json_start = output.find('{')
        json_end = output.rfind('}') + 1
        result_json = json.loads(output[json_start:json_end])
        return result_json
    except Exception:
        return {"raw_output": output}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 package_conversation.py <transcript_text_or_file_path>")
        sys.exit(1)

    input_arg = sys.argv[1]

    # Determine if input is a file path or raw text
    if os.path.isfile(input_arg):
        with open(input_arg, "r") as f:
            transcript = f.read()
        print(f"Loaded transcript from file: {input_arg}")
    else:
        transcript = input_arg
        print("Using provided conversation text.")

    print("\nAnalyzing conversation...")
    data = analyze_conversation(transcript)

    print(f"\nExtracted: {data['title']}")
    print(f"  Date: {data['date']}")
    print(f"  Participants: {data['participants']}")
    print(f"  Action Items: {data['action_item_count']}")
    print(f"  Decisions: {data['decision_count']}")

    print("\nCreating Notion page...")
    result = create_notion_page(data)

    if "pages" in result and result["pages"]:
        page_url = result["pages"][0].get("url", "")
        print(f"\nSuccess! Notion page created: {page_url}")
        print(f"View all packages: {NOTION_ZONE_URL}")
    else:
        print("\nPage creation result:", result)


if __name__ == "__main__":
    main()
