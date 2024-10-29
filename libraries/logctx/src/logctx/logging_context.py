from collections.abc import Generator
from contextlib import contextmanager
from contextvars import ContextVar
from typing import Any


_SCOPES: ContextVar[list[dict[str, Any]]] = ContextVar("scopes", default=[])
"""
Stack of scopes holding the contextual values.
"""


@contextmanager
def logging_scope(**kwargs) -> Generator[None]:
    # TODO: Push scope
    try:
        yield
    finally:
        # TODO: Pop scope
        ...
