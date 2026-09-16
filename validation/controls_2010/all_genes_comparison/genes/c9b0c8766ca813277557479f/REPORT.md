# YIL004C
Status: ok. Length: 589 nt. Measured usable bases: 296. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 296 | 0.3142 | 0.3186 |
| rnafold | ok | 296 | 0.3358 | 0.3562 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 81 | -0.0960 | -0.1902 |
| seed_p | 81 | 0.2166 | 0.1561 |
| seed_p_vs_seed_pars | 46 | -0.0746 | 0.1759 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
