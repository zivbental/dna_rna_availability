# YKL150W
Status: ok. Length: 1163 nt. Measured usable bases: 668. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 668 | 0.3191 | 0.3011 |
| rnafold | ok | 668 | 0.2912 | 0.2628 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 357 | -0.2738 | 0.0871 |
| seed_p | 357 | 0.0846 | 0.0090 |
| seed_p_vs_seed_pars | 239 | 0.0570 | -0.1003 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
