# YKL137W
Status: ok. Length: 540 nt. Measured usable bases: 241. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 241 | 0.3999 | 0.3927 |
| rnafold | ok | 241 | 0.3024 | 0.2680 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 68 | 0.4193 | 0.5461 |
| seed_p | 68 | -0.2769 | -0.3269 |
| seed_p_vs_seed_pars | 56 | -0.4309 | -0.5268 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
