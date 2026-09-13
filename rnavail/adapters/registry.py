"""Adapter discovery and lookup."""

from __future__ import annotations

import importlib
import pkgutil
from typing import Iterable, Iterator, Type

from ..core.result import Tier
from .base import Adapter

_REGISTRY: dict[str, Adapter] = {}
_LOADED = False


def register(cls: Type[Adapter]) -> Type[Adapter]:
    """Class decorator adding an adapter to the global registry."""
    if not cls.name:
        raise ValueError(f"{cls.__name__} must define a non-empty name")
    if cls.name in _REGISTRY:
        raise ValueError(f"duplicate adapter name {cls.name!r}")
    _REGISTRY[cls.name] = cls()
    return cls


def _load_all() -> None:
    """Import every module in this package so decorators fire exactly once."""
    global _LOADED
    if _LOADED:
        return
    _LOADED = True
    package = importlib.import_module(__package__)
    for info in pkgutil.iter_modules(package.__path__):
        if info.name in ("base", "registry", "external"):
            continue
        importlib.import_module(f"{__package__}.{info.name}")


def all_adapters() -> list[Adapter]:
    """Every registered adapter, ordered by tier then cost then name."""
    _load_all()
    return sorted(
        _REGISTRY.values(),
        key=lambda a: (a.tier.order, a.cost, a.name),
    )


def get(name: str) -> Adapter:
    _load_all()
    try:
        return _REGISTRY[name]
    except KeyError:
        raise KeyError(
            f"unknown adapter {name!r}; available: {', '.join(sorted(_REGISTRY))}"
        ) from None


#: Adapters costlier than this are left out of a default run, or ``None`` for
#: no ceiling at all. The scale is wall-clock runtime, not scientific weight.
#: Every adapter currently registered costs 3 or less, so this has no effect
#: today; it exists for a future tool expensive enough to need opting out of.
DEFAULT_MAX_COST = None


def select(
    names: Iterable[str] | None = None,
    tiers: Iterable[Tier] | None = None,
    available_only: bool = True,
    max_cost: int | None = DEFAULT_MAX_COST,
) -> list[Adapter]:
    """Pick adapters by explicit name, by tier, cost and whether they can run.

    Naming adapters explicitly bypasses the cost and availability filters, so
    asking for a specific slow or unavailable tool always gets a visible
    result record from the adapter runner.
    """
    _load_all()
    if names:
        return _filter([get(name) for name in names], tiers, False)
    chosen = all_adapters()
    if max_cost is not None:
        chosen = [a for a in chosen if a.cost <= max_cost]
    return _filter(chosen, tiers, available_only)


def _filter(chosen, tiers, available_only):
    if tiers is not None:
        wanted = set(tiers)
        chosen = [a for a in chosen if a.tier in wanted]
    if available_only:
        chosen = [a for a in chosen if a.availability().available]
    return chosen


def inventory() -> list[dict[str, object]]:
    """Describe every adapter and whether it is usable, for ``rnavail tools``."""
    rows = []
    for adapter in all_adapters():
        status = adapter.availability()
        rows.append({
            "name": adapter.name,
            "tier": adapter.tier.value,
            "available": status.available,
            "version": status.version,
            "reason": status.reason,
            "hint": status.hint,
            "cost": adapter.cost,
            "description": adapter.description,
            "provides": list(adapter.provides),
            "model_family": adapter.model_family or adapter.name,
            "algorithm": adapter.algorithm or adapter.name,
            "probing_methods": sorted(adapter.probing_methods),
            "applied_settings": sorted(adapter.applied_setting_names),
        })
    return rows
