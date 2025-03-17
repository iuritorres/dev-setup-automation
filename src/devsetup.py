"""Main module of the project."""

import os
from argparse import Namespace

import configs
from cli import setup_cli_args
from configs.utils import get_config_functions


def setup(args: Namespace):
    """Setup the project."""

    setup_configs = []
    setup_configs.append(args.configs)

    if len(setup_configs) == 0 or setup_configs[0] is None:
        setup_configs = configs.__all__

    for config in setup_configs:

        config_module = getattr(configs, config)
        config_functions = get_config_functions(config_module)

        for function in config_functions:
            function()


if __name__ == "__main__":
    os.system("clear")

    cli_args = setup_cli_args()
    setup(cli_args)
