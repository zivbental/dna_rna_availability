# YMR307W
Status: ok. Length: 1931 nt. Measured usable bases: 1787. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1787 | 0.3264 | 0.3119 |
| rnafold | ok | 1787 | 0.2284 | 0.2248 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1741 | -0.1014 | -0.1643 |
| seed_p | 1741 | -0.2666 | -0.2073 |
| seed_p_vs_seed_pars | 1657 | -0.2963 | -0.2523 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
