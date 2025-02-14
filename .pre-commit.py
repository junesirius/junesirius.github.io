#!/usr/bin/python
# encoding=utf-8
import subprocess
import sys
from pathlib import Path

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

            # Check empty paragraphs
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

            # Check if images using relative path
            if "](/assets/images" in content or "](assets/images" in content:
                if file not in file_changed:
                    file_changed.append(file)
                print(
                    colored(
                        "\n\tNote: Images using relative path found!"
                        "\n\tWarning: Starting to edit file content...",
                        "red",
                    ),
                    end="",
                )
                content = content.replace(
                    "](/assets/images",
                    "](https://raw.githubusercontent.com/junesirius/junesirius.github.io/master/assets/images",
                )
                content = content.replace(
                    "](assets/images",
                    "](https://raw.githubusercontent.com/junesirius/junesirius.github.io/master/assets/images",
                )
                with file.open("w", encoding="utf-8") as f:
                    f.write(content)

            # Check line not ends with space
            with file.open("r", encoding="utf-8") as f:
                lines = f.readlines()
            file_need_change = False
            is_front_format = True
            new_lines = []
            for idx, line in enumerate(lines):
                # skip checking front format
                if idx == 0:
                    new_lines.append(line)
                    continue
                if line == "---\n":
                    is_front_format = False
                if is_front_format:
                    new_lines.append(line)
                    continue

                if line.endswith(" \n"):
                    file_need_change = True
                    new_lines.append(line.replace("\n", "").rstrip(" ") + "\n")
                else:
                    new_lines.append(line)
            if file_need_change:
                if file not in file_changed:
                    file_changed.append(file)
                print(
                    colored(
                        "\n\tNote: Line ends with space found!"
                        "\n\tWarning: Starting to edit file content...",
                        "red",
                    ),
                    end="",
                )
                with file.open("w", encoding="utf-8") as f:
                    for line in new_lines:
                        f.write(line)
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
