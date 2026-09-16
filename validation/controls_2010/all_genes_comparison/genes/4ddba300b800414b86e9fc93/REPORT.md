# YMR226C
Status: ok. Length: 872 nt. Measured usable bases: 710. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 710 | 0.3528 | 0.3451 |
| rnafold | ok | 710 | 0.2887 | 0.2942 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 602 | -0.1500 | -0.4553 |
| seed_p | 602 | -0.1140 | -0.2876 |
| seed_p_vs_seed_pars | 522 | -0.1137 | -0.2742 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
