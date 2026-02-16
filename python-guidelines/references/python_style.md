# Python Style Reference

## Core code style

1. Write concise, clean, nicely formatted code.
2. Prefer Pythonic patterns, conventional naming, and straightforward control flow.
3. Avoid poor names (e.g., single-letter variables), except in common short-scope conventions (e.g., i/j for loops, x/y for coordinates, f for file handles, e for exceptions).
4. Add concise, helpful comments where appropriate (e.g., code blocks or conditional branches) to improve readability and maintainability.
5. Order code (e.g., constants, classes, functions) in a conventional, logical sequence. Do not mirror the user prompt order unless the user explicitly asks.

## String formatting (f-strings)

1. Prefer f-strings for interpolation over %-style formatting, `str.format()`, and `string.Template`.
2. Use debug-style expressions (`{name=}`) when the rendered output is equivalent to writing the variable name explicitly.
3. Keep explicit labels when the label text is not the same as the expression.
4. Use f-string format specifiers when formatting values (including datetimes) instead of separate formatting calls when behavior is equivalent.
5. In print or log messages, quote code identifiers to distinguish code terms from normal prose. Prefer `!r` (e.g., `f"{name!r}"`) over manual quote wrapping.

Examples:
- Prefer `f"{request_id=}"` over `f"request_id={request_id}"`.
- Keep `f"http_status={status_code}"` as-is (do not rewrite to `f"{status_code=}"`).
- Prefer `f"{created_at:%Y-%m-%d %H:%M:%S}"` over `created_at.strftime("%Y-%m-%d %H:%M:%S")` when used only to build the same string.
- Prefer `logger.info(f"Skipping {func_name!r}: missing {config_key!r}")` over `logger.info(f"Skipping '{func_name}': missing '{config_key}'")`.

## Typing

1. Prefer built-in collection types for type hints (`list`, `dict`, `tuple`, `set`).
2. Import from `typing` only when necessary.
3. Add type hints when inference is unclear (e.g., empty collection initialization), but avoid redundant annotations that reduce clarity.

## File-level conventions

1. Do not add a shebang line or encoding declaration unless the user explicitly asks.
2. Follow the formatting style shown below.
3. If not covered here, follow official PEP recommendations. If still ambiguous, choose the most commonly used conventional style.

## Full Python Style Example

```python
"""Minimal formatting example (PEP 8 + common conventions).

Notes:
- Comments use no trailing period
- Docstrings are complete sentences and end with a period
"""

DEFAULT_LIMIT: int = 10  # Inline comment, no period


def clamp(value: int, low: int = 0, high: int = DEFAULT_LIMIT) -> int:
    """Return value limited to the inclusive range [low, high]."""
    if value < low:
        return low

    if value > high:
        return high

    return value


def format_user(name: str, tags: list[str] | None = None) -> str:
    """Format a user label.

    Args:
        name: Display name to format.
        tags: Optional tag strings.

    Returns:
        A formatted label string.
    """
    cleaned_name = name.strip()

    # Normalize None to an empty list
    tag_list: list[str] = tags or []

    suffix = f" ({', '.join(tag_list)})" if tag_list else ""
    return f"{cleaned_name}{suffix}"


def count_words(lines: list[str]) -> dict[str, int]:
    """Count case-insensitive word frequency from lines."""
    counts: dict[str, int] = {}

    for line in lines:
        # Split on whitespace for a lightweight example
        for raw in line.split():
            word = raw.casefold()
            counts[word] = counts.get(word, 0) + 1

    return counts


def main() -> None:
    """Run a tiny demo."""
    # Single-line comment, no period
    label = format_user("  Ada  ", tags=["admin", "active"])
    limited = clamp(42)

    print(label)
    print(limited)


if __name__ == "__main__":
    main()
```
