# YPL176C
Status: ok. Length: 2485 nt. Measured usable bases: 1255. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1255 | 0.3003 | 0.2852 |
| rnafold | ok | 1255 | 0.2334 | 0.2346 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 175 | -0.1715 | -0.0624 |
| seed_p | 175 | 0.0209 | 0.0334 |
| seed_p_vs_seed_pars | 136 | 0.1114 | 0.1512 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
