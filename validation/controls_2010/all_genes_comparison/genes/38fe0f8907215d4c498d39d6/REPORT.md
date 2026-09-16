# YGL198W
Status: ok. Length: 758 nt. Measured usable bases: 590. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 590 | 0.2711 | 0.2615 |
| rnafold | ok | 590 | 0.2026 | 0.2009 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 435 | -0.1616 | -0.1642 |
| seed_p | 435 | -0.0444 | -0.1055 |
| seed_p_vs_seed_pars | 351 | -0.0994 | -0.1618 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
