# YLR078C
Status: ok. Length: 861 nt. Measured usable bases: 414. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 414 | 0.4531 | 0.4611 |
| rnafold | ok | 414 | 0.4500 | 0.4638 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | -0.2373 | -0.6619 |
| seed_p | 62 | -0.3612 | -0.4327 |
| seed_p_vs_seed_pars | 44 | -0.4815 | -0.6900 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
