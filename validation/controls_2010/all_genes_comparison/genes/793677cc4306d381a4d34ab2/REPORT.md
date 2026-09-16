# YGL040C
Status: ok. Length: 1290 nt. Measured usable bases: 994. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 994 | 0.2381 | 0.2255 |
| rnafold | ok | 994 | 0.1850 | 0.1823 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 790 | 0.0287 | -0.1698 |
| seed_p | 790 | -0.0974 | -0.1771 |
| seed_p_vs_seed_pars | 634 | -0.0417 | -0.1230 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
