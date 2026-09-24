import random
import time
from pathlib import Path

import pydirectinput


# =========================
# SETTINGS
# =========================

TEXT_FILE = "Text.txt"

# Delay before typing starts
START_DELAY = 3.0

# Delay between regular characters
CHAR_DELAY_MIN = 0.04
CHAR_DELAY_MAX = 0.08

# Delay after spaces
SPACE_DELAY_MIN = 0.04
SPACE_DELAY_MAX = 0.10

# Delay after punctuation
PUNCT_DELAY_MIN = 0.08
PUNCT_DELAY_MAX = 0.16

# Delay after line breaks
ENTER_DELAY_MIN = 0.15
ENTER_DELAY_MAX = 0.30

# Delay after tabs
TAB_DELAY_MIN = 0.08
TAB_DELAY_MAX = 0.15


# =========================
# TEXT INPUT
# =========================

def type_unicode_char(char):
    """Type one Unicode character."""
    pydirectinput.unicode_press(char, _pause=False)


# =========================
# RANDOM DELAY
# =========================

def random_delay(min_delay, max_delay):
    time.sleep(random.uniform(min_delay, max_delay))


def delay_after(char):
    """Apply a delay depending on the character type."""

    if char == " ":
        random_delay(
            SPACE_DELAY_MIN,
            SPACE_DELAY_MAX
        )

    elif char == "\t":
        random_delay(
            TAB_DELAY_MIN,
            TAB_DELAY_MAX
        )

    elif char in ".,!?;:)]}\"'»…":
        random_delay(
            PUNCT_DELAY_MIN,
            PUNCT_DELAY_MAX
        )

    elif char == "\n":
        random_delay(
            ENTER_DELAY_MIN,
            ENTER_DELAY_MAX
        )

    else:
        random_delay(
            CHAR_DELAY_MIN,
            CHAR_DELAY_MAX
        )


# =========================
# MAIN
# =========================

def main():

    file_path = Path(__file__).parent / TEXT_FILE

    if not file_path.exists():
        print(f"File not found: {TEXT_FILE}")
        return

    # Keep line endings exactly as they are in the file
    with open(
        file_path,
        "r",
        encoding="utf-8",
        newline=""
    ) as file:
        text = file.read()

    if not text:
        print("The file is empty.")
        return

    print(f"Characters to type: {len(text)}")
    print(f"Starting in {START_DELAY} seconds...")

    # Give the user time to switch to Google Docs
    time.sleep(START_DELAY)

    for char in text:

        # Ignore CR from Windows CRLF line endings
        if char == "\r":
            continue

        # Handle line breaks
        if char == "\n":
            pydirectinput.press(
                "enter",
                _pause=False
            )

        # Handle tabs
        elif char == "\t":
            pydirectinput.press(
                "tab",
                _pause=False
            )

        # Handle all other Unicode characters
        else:
            type_unicode_char(char)

        delay_after(char)

    print("Finished!")


if __name__ == "__main__":
    main()