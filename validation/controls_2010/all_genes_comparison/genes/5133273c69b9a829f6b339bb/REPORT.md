# YGL215W
Status: ok. Length: 2126 nt. Measured usable bases: 982. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 982 | 0.2199 | 0.1941 |
| rnafold | ok | 982 | 0.2364 | 0.2337 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 200 | -0.0598 | -0.0861 |
| seed_p | 200 | 0.0213 | -0.0589 |
| seed_p_vs_seed_pars | 142 | -0.0110 | -0.1147 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
