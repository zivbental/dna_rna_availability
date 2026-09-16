# YER117W
Status: ok. Length: 510 nt. Measured usable bases: 251. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 251 | 0.3704 | 0.3677 |
| rnafold | ok | 251 | 0.3116 | 0.3340 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 142 | -0.3378 | -0.4047 |
| seed_p | 142 | -0.5932 | -0.5819 |
| seed_p_vs_seed_pars | 129 | -0.3807 | -0.2955 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
