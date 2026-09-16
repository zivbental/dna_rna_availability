# YBR084C-A
Status: ok. Length: 796 nt. Measured usable bases: 383. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 383 | 0.4830 | 0.4725 |
| rnafold | ok | 383 | 0.4358 | 0.4353 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 242 | -0.3133 | -0.3733 |
| seed_p | 242 | -0.1661 | -0.1815 |
| seed_p_vs_seed_pars | 186 | -0.2130 | -0.1602 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
