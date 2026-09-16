# YDL164C
Status: ok. Length: 2452 nt. Measured usable bases: 1042. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1042 | 0.3601 | 0.3387 |
| rnafold | ok | 1042 | 0.3309 | 0.3017 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 111 | 0.0553 | -0.0766 |
| seed_p | 111 | 0.0518 | -0.1371 |
| seed_p_vs_seed_pars | 65 | 0.0443 | 0.0248 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
