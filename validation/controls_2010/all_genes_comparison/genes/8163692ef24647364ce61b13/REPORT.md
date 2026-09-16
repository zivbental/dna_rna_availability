# YIL106W
Status: ok. Length: 1131 nt. Measured usable bases: 440. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 440 | 0.2356 | 0.2206 |
| rnafold | ok | 440 | 0.1906 | 0.1809 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 36 | -0.3881 | -0.6164 |
| seed_p | 36 | -0.4826 | -0.4901 |
| seed_p_vs_seed_pars | 24 | -0.5301 | -0.8826 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
