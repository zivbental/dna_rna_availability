# YBR181C
Status: ok. Length: 810 nt. Measured usable bases: 118. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 118 | 0.2986 | 0.2754 |
| rnafold | ok | 118 | 0.2890 | 0.2660 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 49 | 0.0509 | 0.2431 |
| seed_p | 49 | 0.1799 | 0.2244 |
| seed_p_vs_seed_pars | 43 | -0.1976 | -0.4450 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
