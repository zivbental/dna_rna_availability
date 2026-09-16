# YOR239W
Status: ok. Length: 2140 nt. Measured usable bases: 929. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 929 | 0.4285 | 0.4271 |
| rnafold | ok | 929 | 0.3663 | 0.3557 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 157 | -0.0613 | -0.1417 |
| seed_p | 157 | -0.3806 | -0.2341 |
| seed_p_vs_seed_pars | 124 | -0.5650 | -0.3381 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
