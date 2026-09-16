# YJL041W
Status: ok. Length: 2660 nt. Measured usable bases: 1148. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1148 | 0.0416 | 0.0469 |
| rnafold | ok | 1148 | 0.0497 | 0.0587 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 146 | -0.1633 | -0.0702 |
| seed_p | 146 | -0.5434 | -0.2404 |
| seed_p_vs_seed_pars | 106 | -0.5557 | -0.2837 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
