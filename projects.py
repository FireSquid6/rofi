#!/bin/python3
import rofi_menu
import os

applications = {
    "code": "code",
    "codium": "codium",
}


class Menu(rofi_menu.Menu):
    prompt = "Quick Access"
    items = [
        rofi_menu.ShellItem("edit: config", "code /home/firesquid/.config/"),
        rofi_menu.ShellItem("edit: personal files", "code /home/firesquid/personal/")
    ]
    for application in applications:
        items.append(rofi_menu.ShellItem(
            f"open: {application}", applications[application]))

    directory = "/home/firesquid/source"
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            items.append(rofi_menu.ShellItem(
                f"project: {filename}", f"code {directory}/{filename}"))


if __name__ == "__main__":
    rofi_menu.run(Menu(), rofi_version="1.7.1")
