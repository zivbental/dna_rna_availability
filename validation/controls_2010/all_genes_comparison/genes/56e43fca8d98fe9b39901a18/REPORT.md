# YLR344W
Status: ok. Length: 527 nt. Measured usable bases: 306. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 306 | 0.4002 | 0.4115 |
| rnafold | ok | 306 | 0.3244 | 0.3624 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 191 | -0.4426 | -0.6380 |
| seed_p | 191 | -0.4406 | -0.4659 |
| seed_p_vs_seed_pars | 157 | -0.4869 | -0.5152 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
