# Python Style Reference

1. Write concise, clean, nicely formatted code.
2. Add concise, helpful comments for maintainability and readability.
3. Prefer conventional, Pythonic naming and structure. Avoid poor names (for example, single-letter variables), except in common short-scope conventions (like i/j for loops, x/y for coordinates, f for file handles, e for exceptions).
4. Prefer Pythonic patterns and straightforward control flow.
5. Order code (e.g., classes, functions, constants) in a conventional, logical sequence; choose the optimal ordering instead of mirroring the user prompt unless the user specifies otherwise.
6. Prefer built-in collection types for type hints (list, dict, tuple, set). Import from typing only when necessary.
7. Do not add a shebang line or encoding declaration unless the user explicitly asks.
8. Follow the formatting style shown below. If not covered here, follow the official PEP recommendations, and if still ambiguous, choose the most commonly used conventional style.

## Formatting example placeholder

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
    tag_list = tags or []

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
