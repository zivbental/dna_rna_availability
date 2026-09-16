# YHL001W
Status: ok. Length: 563 nt. Measured usable bases: 237. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 237 | 0.4374 | 0.4400 |
| rnafold | ok | 237 | 0.2644 | 0.2781 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 126 | -0.5890 | -0.6892 |
| seed_p | 126 | -0.7874 | -0.7726 |
| seed_p_vs_seed_pars | 81 | -0.5470 | -0.5273 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
