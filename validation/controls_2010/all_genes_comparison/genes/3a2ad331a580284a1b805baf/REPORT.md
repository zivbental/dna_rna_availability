# YIL014W
Status: ok. Length: 2046 nt. Measured usable bases: 826. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 826 | 0.2942 | 0.2860 |
| rnafold | ok | 826 | 0.2756 | 0.2454 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | 0.3073 | 0.5603 |
| seed_p | 51 | -0.0391 | -0.0687 |
| seed_p_vs_seed_pars | 39 | -0.8723 | -0.9041 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
