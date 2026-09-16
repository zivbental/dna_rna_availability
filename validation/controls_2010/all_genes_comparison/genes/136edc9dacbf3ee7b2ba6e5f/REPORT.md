# YDL088C
Status: ok. Length: 1877 nt. Measured usable bases: 705. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 705 | 0.2933 | 0.2808 |
| rnafold | ok | 705 | 0.2371 | 0.2407 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 104 | 0.0766 | 0.1946 |
| seed_p | 104 | 0.0873 | 0.2062 |
| seed_p_vs_seed_pars | 82 | -0.0996 | -0.0797 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
