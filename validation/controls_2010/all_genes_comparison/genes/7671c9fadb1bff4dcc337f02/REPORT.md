# YDR496C
Status: ok. Length: 2057 nt. Measured usable bases: 863. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 863 | 0.3269 | 0.3115 |
| rnafold | ok | 863 | 0.2990 | 0.2845 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | -0.1878 | -0.0753 |
| seed_p | 87 | -0.5307 | -0.3844 |
| seed_p_vs_seed_pars | 65 | -0.8323 | -0.7537 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
