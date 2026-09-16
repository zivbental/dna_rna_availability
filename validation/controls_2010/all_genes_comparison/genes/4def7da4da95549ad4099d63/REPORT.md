# YPL031C
Status: ok. Length: 1005 nt. Measured usable bases: 629. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 629 | 0.2842 | 0.2844 |
| rnafold | ok | 629 | 0.2536 | 0.2605 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 247 | 0.0071 | -0.1552 |
| seed_p | 247 | 0.0582 | -0.0554 |
| seed_p_vs_seed_pars | 202 | 0.0548 | -0.0354 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
