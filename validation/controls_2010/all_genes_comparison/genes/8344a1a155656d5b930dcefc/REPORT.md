# YGL047W
Status: ok. Length: 670 nt. Measured usable bases: 316. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 316 | 0.3128 | 0.3133 |
| rnafold | ok | 316 | 0.3313 | 0.3277 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 26 | -0.0164 | 0.0766 |
| seed_p | 26 | 0.0259 | -0.1876 |
| seed_p_vs_seed_pars | 19 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
