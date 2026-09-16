# YMR292W
Status: ok. Length: 559 nt. Measured usable bases: 323. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 323 | 0.2331 | 0.2135 |
| rnafold | ok | 323 | 0.2013 | 0.1952 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 130 | -0.1210 | -0.2262 |
| seed_p | 130 | -0.0826 | -0.0773 |
| seed_p_vs_seed_pars | 80 | 0.1579 | -0.0152 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
