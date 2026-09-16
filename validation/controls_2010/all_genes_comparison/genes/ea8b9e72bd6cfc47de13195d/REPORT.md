# YHL027W
Status: ok. Length: 2198 nt. Measured usable bases: 965. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 965 | 0.2863 | 0.2824 |
| rnafold | ok | 965 | 0.2260 | 0.2236 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | 0.0413 | -0.2227 |
| seed_p | 135 | -0.3139 | -0.3254 |
| seed_p_vs_seed_pars | 91 | -0.3490 | -0.4537 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
