# YNL138W-A
Status: ok. Length: 406 nt. Measured usable bases: 171. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 171 | 0.2599 | 0.2567 |
| rnafold | ok | 171 | 0.3564 | 0.3486 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | 0.2234 | -0.0052 |
| seed_p | 51 | 0.2290 | 0.2427 |
| seed_p_vs_seed_pars | 39 | 0.4954 | 0.5343 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
