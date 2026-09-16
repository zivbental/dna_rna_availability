# YNL246W
Status: ok. Length: 1099 nt. Measured usable bases: 750. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 750 | 0.3259 | 0.3167 |
| rnafold | ok | 750 | 0.3092 | 0.3085 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 413 | -0.1637 | -0.1385 |
| seed_p | 413 | -0.1664 | -0.0480 |
| seed_p_vs_seed_pars | 317 | 0.0562 | 0.1795 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
