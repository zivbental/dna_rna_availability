# YBR230C
Status: ok. Length: 430 nt. Measured usable bases: 295. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 295 | 0.2975 | 0.2568 |
| rnafold | ok | 295 | 0.2357 | 0.1926 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 145 | -0.4772 | -0.5235 |
| seed_p | 145 | -0.4529 | -0.4519 |
| seed_p_vs_seed_pars | 118 | -0.6512 | -0.6912 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
