"""Main module of the project."""

import os

from configs import vscode

if __name__ == "__main__":
    os.system("clear")

    vscode.install_extensions()
    vscode.setup_settings()
    vscode.setup_keybindings()
