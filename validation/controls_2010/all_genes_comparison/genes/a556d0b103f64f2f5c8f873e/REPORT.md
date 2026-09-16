# YBR091C
Status: ok. Length: 444 nt. Measured usable bases: 231. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 231 | 0.3748 | 0.3701 |
| rnafold | ok | 231 | 0.3300 | 0.3292 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 40 | 0.6615 | 0.5293 |
| seed_p | 40 | 0.4704 | 0.6810 |
| seed_p_vs_seed_pars | 37 | 0.5980 | 0.5434 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
