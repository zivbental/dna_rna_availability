# YBR145W
Status: ok. Length: 1219 nt. Measured usable bases: 404. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 404 | 0.2172 | 0.2116 |
| rnafold | ok | 404 | 0.2438 | 0.2048 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 28 | 0.1619 | -0.2421 |
| seed_p | 28 | -0.5877 | -0.6102 |
| seed_p_vs_seed_pars | 11 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
