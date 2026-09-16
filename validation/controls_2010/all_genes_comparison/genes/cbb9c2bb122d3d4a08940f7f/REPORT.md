# YOR221C
Status: ok. Length: 1296 nt. Measured usable bases: 439. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 439 | 0.1891 | 0.1976 |
| rnafold | ok | 439 | 0.2298 | 0.2326 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 38 | -0.5887 | -0.7735 |
| seed_p | 38 | -0.6067 | -0.6355 |
| seed_p_vs_seed_pars | 18 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
