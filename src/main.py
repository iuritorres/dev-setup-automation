"""Main module of the project."""

import os

from configs import terminal, vscode
from configs.utils import get_config_functions

if __name__ == "__main__":
    os.system("clear")

    vscode_configs = get_config_functions(vscode)
    terminal_configs = get_config_functions(terminal)

    for config in [*vscode_configs, *terminal_configs]:
        config()
