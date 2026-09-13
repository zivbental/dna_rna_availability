"""Thermodynamic conversions shared by every adapter.

The single quantity the whole pipeline is organised around is the *joint*
probability that a target interval is simultaneously unpaired,

    P_unpaired(i, j) = P(all nucleotides i..j are unpaired)

and its equivalent opening penalty

    dG_open(i, j) = -RT * ln P_unpaired(i, j)

Note that this is deliberately NOT the mean of per-nucleotide unpaired
probabilities: a 20 nt binding site needs a simultaneously available
nucleation region, not twenty nucleotides that happen to be free at
different times.
"""

from __future__ import annotations

import math

#: Gas constant in kcal/(mol*K), matching the units ViennaRNA reports energies in.
GAS_CONSTANT_KCAL = 0.0019872041

def rt(temperature_c: float = 37.0) -> float:
    """Return RT in kcal/mol at the given temperature in degrees Celsius."""
    return GAS_CONSTANT_KCAL * (temperature_c + 273.15)


def dg_open_from_probability(p_unpaired: float, temperature_c: float = 37.0) -> float:
    """Convert a joint unpaired probability into an opening free energy.

    Zero maps to positive infinity. Callers that cannot distinguish a true
    zero from numerical underflow must record that censoring explicitly rather
    than turn it into an ordinary finite point estimate.
    """
    if p_unpaired is None or not math.isfinite(p_unpaired):
        return float("nan")
    if p_unpaired < 0.0 or p_unpaired > 1.0:
        return float("nan")
    if p_unpaired == 0.0:
        return math.inf
    return -rt(temperature_c) * math.log(p_unpaired)


def probability_from_dg_open(dg_open: float, temperature_c: float = 37.0) -> float:
    """Inverse of :func:`dg_open_from_probability`."""
    if dg_open is None or not math.isfinite(dg_open):
        return float("nan")
    exponent = -dg_open / rt(temperature_c)
    # A negative opening energy is a numerical/model inconsistency, not a
    # probability above one. Avoid overflow while retaining the observable's
    # physical bound.
    if exponent >= 0.0:
        return 1.0
    # binary64 underflows below roughly -745. Callers serializing this inverse
    # conversion retain the resulting zero as a censored probability.
    if exponent < -745.0:
        return 0.0
    return math.exp(exponent)


def dg_open_per_nucleotide(dg_open: float, length: int) -> float:
    """Length-normalised opening penalty, for comparing sites of unequal size.

    A 30 nt window will almost always cost more to open than a 12 nt window,
    so raw dG_open cannot be compared across different target lengths.
    """
    if length <= 0 or dg_open is None or not math.isfinite(dg_open):
        return float("nan")
    return dg_open / length


def boltzmann_weight(dg: float, temperature_c: float = 37.0) -> float:
    """exp(-dG/RT), guarded against overflow for very favourable energies."""
    if dg is None or not math.isfinite(dg):
        return float("nan")
    exponent = -dg / rt(temperature_c)
    if exponent > 700.0:          # math.exp overflows past ~709
        return math.inf
    return math.exp(exponent)
