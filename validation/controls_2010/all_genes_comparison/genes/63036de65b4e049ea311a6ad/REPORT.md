# YDR404C
Status: ok. Length: 835 nt. Measured usable bases: 610. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 610 | 0.1898 | 0.1825 |
| rnafold | ok | 610 | 0.1632 | 0.1670 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 333 | 0.0843 | -0.1928 |
| seed_p | 333 | 0.0108 | -0.0403 |
| seed_p_vs_seed_pars | 273 | -0.1258 | -0.1259 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
