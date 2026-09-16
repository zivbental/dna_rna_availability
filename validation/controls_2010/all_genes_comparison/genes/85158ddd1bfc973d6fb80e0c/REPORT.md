# YKL106W
Status: ok. Length: 1604 nt. Measured usable bases: 886. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 886 | 0.2953 | 0.2767 |
| rnafold | ok | 886 | 0.2240 | 0.2372 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 287 | -0.5357 | -0.2084 |
| seed_p | 287 | -0.1471 | -0.0783 |
| seed_p_vs_seed_pars | 238 | -0.3416 | -0.3675 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
