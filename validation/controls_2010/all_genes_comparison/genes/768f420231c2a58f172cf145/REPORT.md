# YLR048W
Status: ok. Length: 1176 nt. Measured usable bases: 720. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 720 | 0.2869 | 0.2682 |
| rnafold | ok | 720 | 0.2448 | 0.2223 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 449 | -0.0597 | -0.1588 |
| seed_p | 449 | -0.0015 | 0.0344 |
| seed_p_vs_seed_pars | 421 | 0.0494 | 0.0567 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
