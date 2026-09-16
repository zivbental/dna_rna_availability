# YDL160C
Status: ok. Length: 1852 nt. Measured usable bases: 1095. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1095 | 0.2032 | 0.1829 |
| rnafold | ok | 1095 | 0.2213 | 0.2002 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 390 | -0.1455 | 0.0330 |
| seed_p | 390 | -0.1478 | -0.0565 |
| seed_p_vs_seed_pars | 275 | -0.1257 | 0.0089 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
