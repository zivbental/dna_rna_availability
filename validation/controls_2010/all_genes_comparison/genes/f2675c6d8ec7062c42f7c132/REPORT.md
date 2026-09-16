# YGR262C
Status: ok. Length: 893 nt. Measured usable bases: 578. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 578 | 0.3296 | 0.3006 |
| rnafold | ok | 578 | 0.2756 | 0.2542 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 253 | 0.3111 | -0.0609 |
| seed_p | 253 | -0.1513 | -0.1135 |
| seed_p_vs_seed_pars | 191 | -0.0382 | -0.1427 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
