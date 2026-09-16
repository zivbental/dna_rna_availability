# YDL046W
Status: ok. Length: 859 nt. Measured usable bases: 619. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 619 | 0.2825 | 0.2664 |
| rnafold | ok | 619 | 0.2320 | 0.2262 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 379 | -0.2239 | -0.2204 |
| seed_p | 379 | -0.2629 | -0.2050 |
| seed_p_vs_seed_pars | 285 | -0.0889 | 0.0252 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
