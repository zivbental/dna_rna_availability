# YLR177W
Status: ok. Length: 1993 nt. Measured usable bases: 827. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 827 | 0.3065 | 0.3139 |
| rnafold | ok | 827 | 0.2246 | 0.2386 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 55 | -0.1578 | -0.6097 |
| seed_p | 55 | -0.4228 | -0.3681 |
| seed_p_vs_seed_pars | 30 | -0.5240 | -0.5876 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
