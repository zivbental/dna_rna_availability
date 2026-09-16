# YJR112W-A
Status: ok. Length: 462 nt. Measured usable bases: 173. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 173 | 0.3427 | 0.3054 |
| rnafold | ok | 173 | 0.3344 | 0.3502 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 94 | -0.3384 | -0.0485 |
| seed_p | 94 | -0.4633 | -0.2209 |
| seed_p_vs_seed_pars | 72 | -0.4038 | -0.2260 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
