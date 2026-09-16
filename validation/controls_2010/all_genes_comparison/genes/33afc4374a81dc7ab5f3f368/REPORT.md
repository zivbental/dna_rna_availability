# YER088C
Status: ok. Length: 2593 nt. Measured usable bases: 1166. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1166 | 0.2323 | 0.2057 |
| rnafold | ok | 1166 | 0.2113 | 0.1892 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 149 | -0.0957 | -0.1766 |
| seed_p | 149 | -0.5161 | -0.4309 |
| seed_p_vs_seed_pars | 98 | -0.4742 | -0.5363 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
