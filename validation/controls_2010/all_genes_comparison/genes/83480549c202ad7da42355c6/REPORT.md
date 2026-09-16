# YNL322C
Status: ok. Length: 994 nt. Measured usable bases: 738. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 738 | 0.2588 | 0.2499 |
| rnafold | ok | 738 | 0.2566 | 0.2327 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 632 | 0.0538 | 0.1711 |
| seed_p | 632 | -0.0348 | 0.0912 |
| seed_p_vs_seed_pars | 567 | -0.1651 | -0.0602 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
