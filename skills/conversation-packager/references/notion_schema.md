# Notion Database Schema: Conversation Packages

This document defines the schema for the Notion database that stores the packaged conversations.

**Database Name:** Conversation Packages

| Property Name | Type      | Description                                                  |
|---------------|-----------|--------------------------------------------------------------|
| `Title`       | Title     | The title of the conversation (e.g., "Meeting: Q1 Planning") |
| `Date`        | Date      | The date the conversation took place.                        |
| `Topic`       | Text      | The main topic or project the conversation relates to.       |
| `Summary`     | Text      | A concise summary of the conversation.                       |
| `Action Items`| Number    | The number of action items identified in the conversation.   |
| `Decisions`   | Number    | The number of key decisions made in the conversation.        |
| `Participants`| Text      | A comma-separated list of participants in the conversation.  |
