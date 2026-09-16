# YMR142C
Status: ok. Length: 689 nt. Measured usable bases: 430. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 430 | 0.3644 | 0.3625 |
| rnafold | ok | 430 | 0.3598 | 0.3717 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 293 | -0.1868 | -0.0027 |
| seed_p | 293 | -0.1426 | -0.0726 |
| seed_p_vs_seed_pars | 243 | -0.0026 | -0.0728 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
