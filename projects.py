#!/bin/python3
import rofi_menu
import os


EDITOR = "code"


applications = {
    "code": "code",
    "codium": "codium",
    "emacs": "emacs",
}


class Menu(rofi_menu.Menu):
    prompt = "Quick Access"
    items = [
        rofi_menu.ShellItem("edit: config", f"{EDITOR} /home/firesquid/.config/"),
        rofi_menu.ShellItem("edit: personal files", f"{EDITOR} /home/firesquid/personal/")
    ]
    for application in applications:
        items.append(rofi_menu.ShellItem(
            f"open: {application}", applications[application]))

    directory = "/home/firesquid/source"
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            items.append(rofi_menu.ShellItem(
                f"project: {filename}", f"{EDITOR} {directory}/{filename}"))


if __name__ == "__main__":
    rofi_menu.run(Menu(), rofi_version="1.7.1")
