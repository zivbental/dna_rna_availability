# YCL064C
Status: ok. Length: 1180 nt. Measured usable bases: 951. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 951 | 0.3103 | 0.2942 |
| rnafold | ok | 951 | 0.2607 | 0.2523 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 768 | -0.1027 | -0.0203 |
| seed_p | 768 | -0.1275 | -0.1399 |
| seed_p_vs_seed_pars | 696 | -0.2225 | -0.2607 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
