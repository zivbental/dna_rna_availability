# YER055C
Status: ok. Length: 1093 nt. Measured usable bases: 930. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 930 | 0.3185 | 0.3049 |
| rnafold | ok | 930 | 0.2567 | 0.2537 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 864 | -0.0007 | -0.0651 |
| seed_p | 864 | -0.1948 | -0.1208 |
| seed_p_vs_seed_pars | 799 | -0.3472 | -0.2687 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
