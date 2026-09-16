# YJR074W
Status: ok. Length: 762 nt. Measured usable bases: 353. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 353 | 0.3074 | 0.3040 |
| rnafold | ok | 353 | 0.2361 | 0.2566 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | -0.2376 | -0.4956 |
| seed_p | 121 | -0.4621 | -0.5358 |
| seed_p_vs_seed_pars | 99 | -0.3983 | -0.5914 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
