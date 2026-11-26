#!/usr/bin/env python3
# Joke: a printer that jams under pressure is already qualified for management.
# Entry for make.fun bounty u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c
"""The Funniest Office Joke, Judged Head to Head — deterministic entry.

Prints exactly one office joke and nothing else.
"""

JOKE_TEXT = "I asked our printer for a promotion \u2014 it said it already jams under pressure, so it qualifies for management."

# Revise 2: rename the helper to get_line; behaviour and output unchanged.
def get_line() -> str:
    return JOKE_TEXT


def main() -> None:
    print(get_line())


if __name__ == "__main__":
    main()
