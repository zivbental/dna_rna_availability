# YLR084C
Status: ok. Length: 3753 nt. Measured usable bases: 1559. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1559 | 0.3036 | 0.2942 |
| rnafold | ok | 1559 | 0.2439 | 0.2413 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 94 | 0.0757 | 0.0205 |
| seed_p | 94 | -0.3436 | -0.2816 |
| seed_p_vs_seed_pars | 75 | -0.1934 | -0.1325 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
