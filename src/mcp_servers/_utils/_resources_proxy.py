from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `mcp_servers.resources` module.

    This is used so that we can lazily import `mcp_servers.resources` only when
    needed *and* so that users can just import `mcp_servers` and reference `mcp_servers.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("mcp_servers.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
