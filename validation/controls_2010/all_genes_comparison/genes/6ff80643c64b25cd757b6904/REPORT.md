# YMR242C
Status: ok. Length: 690 nt. Measured usable bases: 343. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 343 | 0.2479 | 0.2514 |
| rnafold | ok | 343 | 0.0572 | 0.0771 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | -0.4237 | -0.2433 |
| seed_p | 203 | -0.1484 | -0.2797 |
| seed_p_vs_seed_pars | 157 | -0.2499 | -0.3811 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
