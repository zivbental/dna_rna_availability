# YMR297W
Status: ok. Length: 1785 nt. Measured usable bases: 1578. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1578 | 0.3502 | 0.3213 |
| rnafold | ok | 1578 | 0.3171 | 0.2909 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1512 | -0.1311 | -0.0803 |
| seed_p | 1512 | -0.0466 | -0.0567 |
| seed_p_vs_seed_pars | 1419 | -0.1620 | -0.1680 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
