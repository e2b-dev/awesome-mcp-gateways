#!/usr/bin/env python3
"""Sort list items in README.md alphabetically within each section."""

import re
import sys

def sort_readme(path="README.md"):
    with open(path, "r") as f:
        content = f.read()

    # Split into lines for processing
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        result.append(line)
        i += 1

        # After a heading, collect and sort any list block that follows
        if line.startswith("## "):
            # Collect non-list lines between heading and list (e.g. blank lines)
            while i < len(lines) and not lines[i].startswith("- "):
                result.append(lines[i])
                i += 1

            # Collect list items (may span multiple lines if wrapped)
            items = []
            while i < len(lines) and (lines[i].startswith("- ") or (items and lines[i].startswith("  "))):
                items.append(lines[i])
                i += 1

            # Sort case-insensitively by the link text: - [Name]
            items.sort(key=lambda x: re.sub(r"^- \[", "", x).lower())
            result.extend(items)

    new_content = "\n".join(result)

    if new_content != content:
        with open(path, "w") as f:
            f.write(new_content)
        print("README.md was reordered.")
        return 1
    else:
        print("README.md is already sorted.")
        return 0

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    sort_readme(path)
