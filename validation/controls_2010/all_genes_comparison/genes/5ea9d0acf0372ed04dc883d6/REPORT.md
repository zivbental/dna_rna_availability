# YPL135W
Status: ok. Length: 963 nt. Measured usable bases: 610. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 610 | 0.2393 | 0.2498 |
| rnafold | ok | 610 | 0.1196 | 0.1250 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 443 | -0.2942 | -0.1935 |
| seed_p | 443 | -0.2577 | -0.1978 |
| seed_p_vs_seed_pars | 376 | -0.2188 | -0.2145 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
