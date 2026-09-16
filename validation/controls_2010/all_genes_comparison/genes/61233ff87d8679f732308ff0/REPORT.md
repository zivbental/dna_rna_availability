# YML123C
Status: ok. Length: 1910 nt. Measured usable bases: 1821. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1821 | 0.3245 | 0.3090 |
| rnafold | ok | 1821 | 0.2833 | 0.2724 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1834 | -0.2595 | -0.0705 |
| seed_p | 1834 | -0.1770 | -0.1039 |
| seed_p_vs_seed_pars | 1790 | -0.2953 | -0.2339 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
