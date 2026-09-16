# YDR476C
Status: ok. Length: 864 nt. Measured usable bases: 549. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 549 | 0.2962 | 0.2914 |
| rnafold | ok | 549 | 0.1993 | 0.2199 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 229 | -0.2530 | -0.2922 |
| seed_p | 229 | -0.0056 | -0.0671 |
| seed_p_vs_seed_pars | 187 | -0.0745 | 0.0122 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
