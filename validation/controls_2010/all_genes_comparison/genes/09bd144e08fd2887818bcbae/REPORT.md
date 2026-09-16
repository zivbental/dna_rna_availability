# YJL189W
Status: ok. Length: 321 nt. Measured usable bases: 266. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 266 | 0.2337 | 0.2177 |
| rnafold | ok | 266 | 0.2466 | 0.2022 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 247 | -0.2740 | -0.1937 |
| seed_p | 247 | -0.2527 | -0.3422 |
| seed_p_vs_seed_pars | 227 | -0.3146 | -0.3773 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
