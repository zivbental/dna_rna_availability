# YNL300W
Status: ok. Length: 659 nt. Measured usable bases: 474. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 474 | 0.1935 | 0.1634 |
| rnafold | ok | 474 | 0.1709 | 0.1266 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 317 | -0.3625 | -0.2394 |
| seed_p | 317 | -0.2314 | -0.1956 |
| seed_p_vs_seed_pars | 227 | -0.2907 | -0.2262 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
