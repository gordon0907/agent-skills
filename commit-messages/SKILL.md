---
name: commit-messages
description: Use when the user asks for writing or revising git commit messages.
---

1. Write commit messages with a concise, objective description of *what changed*; do not explain why.
2. Follow the conventional commit format:
   ```text
   <type>(<scope>): <description>
   ```
   where `scope` is optional and `description` is short and imperative.
3. The title should be brief, imperative, and have no trailing period.
4. If additional details are necessary, add them below the title after a blank line, using point form.
5. Use one of the following common commit types:
   - feat
   - fix
   - docs
   - style
   - refactor
   - test
   - chore
6. The latest commit content can be inspected for context with:
   ```bash
   git show
   ```

Example:
```text
feat(parser): add nested expression support

fix(ui): correct login form alignment

docs: update README setup instructions
```
