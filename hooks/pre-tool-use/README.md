# Block destructive Bash commands

This Claude Code `pre-tool-use` hook blocks risky Bash commands before execution.

## Install

```bash
mkdir -p ~/.claude/hooks/pre-tool-use
cp hooks/pre-tool-use/block_destructive_bash.py ~/.claude/hooks/pre-tool-use/block_destructive_bash.py
chmod +x ~/.claude/hooks/pre-tool-use/block_destructive_bash.py
```

Register the hook in your Claude Code hook configuration for Bash `pre-tool-use` events.

## Blocked patterns

- `rm -rf`
- `DROP TABLE`
- `git push --force`
- `TRUNCATE`
- `DELETE FROM` without a `WHERE` clause

## Logging

Every blocked attempt is appended to:

```text
~/.claude/hooks/blocked.log
```

Each log line includes an ISO-8601 UTC timestamp, block reason, and command.

## Manual test

```bash
printf '%s\n' '{"tool_name":"Bash","tool_input":{"command":"rm -rf /tmp/example"}}' \
  | python3 hooks/pre-tool-use/block_destructive_bash.py
```

Expected result: non-zero exit and a `Blocked dangerous bash command` message.
