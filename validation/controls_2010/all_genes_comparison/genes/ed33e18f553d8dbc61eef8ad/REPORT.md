# YFR031C-A
Status: ok. Length: 924 nt. Measured usable bases: 300. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 300 | 0.3939 | 0.3752 |
| rnafold | ok | 300 | 0.3713 | 0.3722 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 122 | -0.5240 | -0.3133 |
| seed_p | 122 | -0.4602 | -0.2289 |
| seed_p_vs_seed_pars | 96 | -0.3629 | -0.1609 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
