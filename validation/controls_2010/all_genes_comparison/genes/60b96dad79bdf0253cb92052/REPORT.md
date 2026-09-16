# YPL090C
Status: ok. Length: 880 nt. Measured usable bases: 153. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 153 | 0.4767 | 0.4959 |
| rnafold | ok | 153 | 0.4052 | 0.4486 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | -0.1478 | -0.1964 |
| seed_p | 72 | 0.0768 | -0.1104 |
| seed_p_vs_seed_pars | 57 | 0.1118 | 0.0340 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
