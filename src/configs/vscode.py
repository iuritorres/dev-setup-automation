"""This module contains functions to setup vscode settings and keybindings"""

from os import system
from pathlib import Path

from github.gist import get_gist

SETTINGS_GIST_ID = "40f561edbad9a102589d5e73cd6df016"
KEYBINDINGS_GIST_ID = "e3c0f38b1cc24ff35ec18dcc914e4892"

config_path = Path.home().joinpath(".config", "Code", "User")


def setup_settings():
    """Setup vscode settings"""

    print("Setting up vscode settings...")

    settings_gist = get_gist(SETTINGS_GIST_ID)
    settings = settings_gist.files["settings.json"].content

    config_path.joinpath("settings.json").write_text(settings, "utf8")


def setup_keybindings():
    """Setup vscode keybindings"""

    print("Setting up vscode keybindings...")

    keybindings_gist = get_gist(KEYBINDINGS_GIST_ID)
    keybindings = keybindings_gist.files["keybindings.json"].content

    config_path.joinpath("keybindings.json").write_text(keybindings, "utf8")


def install_extensions():
    """Install vscode extensions"""

    print("Installing vscode extensions...")

    extensions = [
        # Python Development
        "ms-python.python",
        "ms-python.pylint",
        "ms-python.isort",
        "ms-python.black-formatter",
        "ms-python.vscode-pylance",
        # Linters and Formatters
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "streetsidesoftware.code-spell-checker",
        "streetsidesoftware.code-spell-checker-portuguese-brazilian",
        # Productivity
        "Cardinal90.multi-cursor-case-preserve",
        "yzhang.markdown-all-in-one",
        "YoavBls.pretty-ts-errors",
        "Prisma.prisma",
        "redhat.vscode-yaml",
        "bradlc.vscode-tailwindcss",
        # Themes and Icons
        "dracula-theme.theme-dracula",
        "PKief.material-icon-theme",
        "naumovs.color-highlight",
        # Git Integration
        "eamodio.gitlens",
        # GitHub Integration
        "GitHub.copilot",
        "GitHub.copilot-chat",
    ]

    for extension in extensions:
        system(f"code --install-extension {extension}")
