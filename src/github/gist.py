"""GitHub Gist API."""

from .api import api


def get_gist(gist_id: str):
    """Get a gist."""

    try:
        return api.gists.get(gist_id=gist_id)

    except api.GistNotFoundError:
        print(f"Gist '{gist_id}' not found.")
        return None

    except api.GistAPIError as error:
        print(f"An API error occurred: {error}")
        return None

    except api.RequestError as error:
        print(f"A request error occurred: {error}")
        return None
