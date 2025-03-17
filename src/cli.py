"""Setup the project CLI"""

from argparse import ArgumentParser, Namespace


def setup_cli_args() -> Namespace:
    """Setup the arguments for the CLI."""

    parser = ArgumentParser(description="Setup the development environment.")

    parser.add_argument(
        "-c",
        "--configs",
        type=str,
        choices=["vscode", "terminal"],
        help="Choose the configurations to setup.",
    )

    return parser.parse_args()
