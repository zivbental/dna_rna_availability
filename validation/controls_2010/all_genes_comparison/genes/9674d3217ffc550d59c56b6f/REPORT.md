# YBR078W
Status: ok. Length: 1611 nt. Measured usable bases: 1383. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1383 | 0.2382 | 0.2314 |
| rnafold | ok | 1383 | 0.1973 | 0.1952 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1303 | -0.2139 | -0.1596 |
| seed_p | 1303 | -0.1037 | -0.0661 |
| seed_p_vs_seed_pars | 1170 | -0.0540 | -0.0717 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
