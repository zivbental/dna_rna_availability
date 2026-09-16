# YHR197W
Status: ok. Length: 2405 nt. Measured usable bases: 1007. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1007 | 0.2893 | 0.2940 |
| rnafold | ok | 1007 | 0.2218 | 0.2381 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | -0.0938 | 0.2567 |
| seed_p | 118 | 0.0056 | 0.0710 |
| seed_p_vs_seed_pars | 92 | -0.1463 | -0.0560 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
