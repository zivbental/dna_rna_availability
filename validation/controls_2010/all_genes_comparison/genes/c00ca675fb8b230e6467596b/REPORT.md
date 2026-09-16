# YHR052W
Status: ok. Length: 1291 nt. Measured usable bases: 718. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 718 | 0.3432 | 0.3361 |
| rnafold | ok | 718 | 0.2991 | 0.2947 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 242 | -0.1767 | -0.0183 |
| seed_p | 242 | -0.1307 | -0.0142 |
| seed_p_vs_seed_pars | 185 | -0.3286 | -0.2317 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
