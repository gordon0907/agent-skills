---
name: delete-codex-session
description: Use when the user asks to delete or remove a Codex history/session JSONL under ~/.codex/sessions by session ID.
---

1. Expect the user to provide a session ID such as `019ce5a9-7eaa-7ea2-b8c5-478cb2c2c2d3`.
2. Search only under `~/.codex/sessions` for `.jsonl` filenames containing that exact session ID. Prefer `rg --files ~/.codex/sessions | rg '<session-id>.*\\.jsonl$'`.
3. If the user did not provide a session ID, or the value is obviously malformed, do not search blindly. Ask the user for the exact session ID first.
4. If exactly one `.jsonl` file matches, delete that file and no other files.
5. Never delete files outside `~/.codex/sessions`. Do not delete shell snapshots or any non-`.jsonl` files even if they contain the same ID.
6. If zero matches are found, more than one `.jsonl` file matches, or any other unexpected issue happens, do not delete anything. Tell the user what you found and ask what to do next.
7. If deleting the file requires elevated approval, request it.
8. After a successful deletion, tell the user the exact path that was removed and remind them to restart the Codex app so the removal is reflected.
