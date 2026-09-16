# YDR450W
Status: ok. Length: 583 nt. Measured usable bases: 262. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 262 | 0.4283 | 0.4287 |
| rnafold | ok | 262 | 0.2622 | 0.2411 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 165 | 0.0479 | -0.3819 |
| seed_p | 165 | -0.3366 | -0.4331 |
| seed_p_vs_seed_pars | 152 | -0.1029 | -0.2208 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
