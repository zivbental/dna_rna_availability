# YDR205W
Status: ok. Length: 2284 nt. Measured usable bases: 819. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 819 | 0.2240 | 0.2158 |
| rnafold | ok | 819 | 0.1867 | 0.1711 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 88 | -0.3711 | -0.3140 |
| seed_p | 88 | 0.0001 | -0.0333 |
| seed_p_vs_seed_pars | 47 | -0.0235 | 0.2568 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
