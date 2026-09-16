# YNL130C
Status: ok. Length: 1290 nt. Measured usable bases: 945. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 945 | 0.2925 | 0.2888 |
| rnafold | ok | 945 | 0.2510 | 0.2530 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 710 | -0.3191 | -0.3493 |
| seed_p | 710 | -0.2739 | -0.2330 |
| seed_p_vs_seed_pars | 595 | -0.4123 | -0.4326 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
