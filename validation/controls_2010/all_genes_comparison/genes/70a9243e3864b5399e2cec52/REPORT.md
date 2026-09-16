# YBR048W
Status: ok. Length: 709 nt. Measured usable bases: 382. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 382 | 0.3361 | 0.3503 |
| rnafold | ok | 382 | 0.3879 | 0.4090 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 204 | -0.0183 | -0.3164 |
| seed_p | 204 | -0.1881 | -0.2873 |
| seed_p_vs_seed_pars | 181 | -0.1437 | -0.2217 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
