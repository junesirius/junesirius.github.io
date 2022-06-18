#!/usr/bin/python
# encoding=utf-8
from pathlib import Path
import subprocess
import sys
from termcolor import colored

# print Chinese characters in terminal
sys.stdout.reconfigure(encoding="utf-8")


def check_and_auto_update():
    # Check all files in the staging-area
    file_list = (
        subprocess.Popen(
            "git diff --name-only --staged",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        .communicate()[0]
        .decode("utf-8")
        .split("\n")[:-1]
    )

    file_changed = []

    for file in file_list:
        if (
            file.endswith(".md")
            and not file.endswith("whole-novel.md")
            and not "_drafts" in file
            and Path(file).exists()
        ):
            file = Path(file)
            print(f"Checking {colored(file, 'yellow')} ...", end="")
            with file.open("r", encoding="utf-8") as f:
                content = f.read()
            if "\n" * 4 in content:
                file_changed.append(file)
                print(
                    colored(
                        "\n\tNote: Empty paragraph found!"
                        "\n\tWarning: Starting to edit file content...",
                        "red",
                    ),
                    end="",
                )
                content = content.replace("\n" * 4, "\n\n<br>\n\n")
                with file.open("w", encoding="utf-8") as f:
                    f.write(content)
            print(colored("Done.", "green"))
        else:
            print(f"Skip checking {colored(file, 'yellow')}")

    if file_changed:
        print("\nChanged files: ")
        for file in file_changed:
            print(colored(f"\t{file}", "red"))
        print("\nPlease check file difference and re-commit.\n\n")
        sys.exit(1)


if __name__ == "__main__":
    check_and_auto_update()
