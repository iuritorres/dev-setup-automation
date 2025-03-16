"""Terminal configuration"""

from pathlib import Path

from github.gist import get_gist

SETTINGS_GIST_ID = "1064cd5fc087ad2da70c7ab10122fe5c"

config_path = Path.home()


def setup_powerlevel10k():
    """Setup powerlevel10k"""

    print("Setting up powerlevel10k...")

    settings_gist = get_gist(SETTINGS_GIST_ID)
    settings = settings_gist.files[".p10k.zsh"].content

    config_path.joinpath(".p10k.zsh").write_text(settings, "utf8")
