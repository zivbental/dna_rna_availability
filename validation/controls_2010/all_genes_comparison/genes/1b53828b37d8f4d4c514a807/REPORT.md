# YDR001C
Status: ok. Length: 2542 nt. Measured usable bases: 1150. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1150 | 0.3443 | 0.3249 |
| rnafold | ok | 1150 | 0.2586 | 0.2505 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 167 | -0.3012 | -0.4905 |
| seed_p | 167 | -0.4904 | -0.5330 |
| seed_p_vs_seed_pars | 124 | -0.5545 | -0.5087 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
