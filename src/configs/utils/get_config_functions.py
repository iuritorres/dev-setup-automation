"""Get all functions from a module."""

import inspect
from types import FunctionType
from typing import List


def get_config_functions(module: object) -> List[FunctionType]:
    """Get all functions from a module."""

    module_members = inspect.getmembers(module, inspect.isfunction)

    functions = []

    for _, function in module_members:
        if function.__module__ == module.__name__:
            functions.append(function)

    return functions
