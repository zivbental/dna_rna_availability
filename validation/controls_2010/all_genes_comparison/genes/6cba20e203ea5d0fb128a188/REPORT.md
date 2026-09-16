# YIL052C
Status: ok. Length: 426 nt. Measured usable bases: 247. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 247 | 0.4004 | 0.3944 |
| rnafold | ok | 247 | 0.3399 | 0.3860 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 187 | 0.0414 | -0.4047 |
| seed_p | 187 | -0.1489 | -0.3360 |
| seed_p_vs_seed_pars | 165 | -0.2776 | -0.3363 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
