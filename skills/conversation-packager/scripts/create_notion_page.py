#!/usr/bin/env python

import json
import os
import sys


def main():
    if len(sys.argv) != 7:
        print("Usage: create_notion_page.py <title> <date> <topic> <summary> <action_items> <participants>")
        sys.exit(1)

    database_id = "ab27ee0b-a371-4260-9814-8d512569a6bf"
    title = sys.argv[1]
    date = sys.argv[2]
    topic = sys.argv[3]
    summary = sys.argv[4]
    action_items = sys.argv[5]
    participants = sys.argv[6]

    # Read the template
    with open("/home/ubuntu/skills/conversation-packager/templates/notion_page_template.md", "r") as f:
        template = f.read()

    # Fill the template
    content = template.format(
        title=title,
        date=date,
        topic=topic,
        summary=summary,
        action_items=action_items,
        key_decisions="",  # Placeholder for now
        participants=participants
    )

    # Construct the API call
    pages = [
        {
            "properties": {
                "Title": title,
                "date:Date:start": date,
                "Topic": topic,
                "Summary": summary,
                "Action Items": len(action_items.split("\n")) if action_items else 0,
                "Decisions": 0,
                "Participants": participants
            },
            "content": content
        }
    ]

    parent = {"data_source_id": database_id}

    input_json = {
        "parent": parent,
        "pages": pages
    }

    # Create the command
    command = (
        f"manus-mcp-cli tool call notion-create-pages --server notion --input '{json.dumps(input_json)}'"
    )

    # Execute the command
    os.system(command)


if __name__ == "__main__":
    main()
