# YMR230W
Status: ok. Length: 444 nt. Measured usable bases: 272. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 272 | 0.3578 | 0.3493 |
| rnafold | ok | 272 | 0.2521 | 0.2506 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | -0.1275 | -0.1709 |
| seed_p | 143 | -0.3974 | -0.4174 |
| seed_p_vs_seed_pars | 141 | -0.4561 | -0.4621 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
