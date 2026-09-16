# YFL034C-A
Status: ok. Length: 460 nt. Measured usable bases: 337. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 337 | 0.2962 | 0.2873 |
| rnafold | ok | 337 | 0.2397 | 0.2356 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 281 | 0.0473 | -0.1082 |
| seed_p | 281 | -0.2335 | -0.2073 |
| seed_p_vs_seed_pars | 207 | -0.4091 | -0.3911 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
