# YLR093C
Status: ok. Length: 851 nt. Measured usable bases: 479. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 479 | 0.3426 | 0.3422 |
| rnafold | ok | 479 | 0.2024 | 0.2530 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 157 | -0.1852 | 0.1463 |
| seed_p | 157 | 0.1276 | 0.1432 |
| seed_p_vs_seed_pars | 135 | 0.0554 | -0.0219 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
