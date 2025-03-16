"""Main module of the project."""

import os

from configs import terminal, vscode

if __name__ == "__main__":
    os.system("clear")

    terminal.setup_powerlevel10k()

    vscode.install_extensions()
    vscode.setup_settings()
    vscode.setup_keybindings()
