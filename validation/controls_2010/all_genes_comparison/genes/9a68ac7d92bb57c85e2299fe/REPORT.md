# YNR046W
Status: ok. Length: 560 nt. Measured usable bases: 478. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 478 | 0.2864 | 0.2825 |
| rnafold | ok | 478 | 0.3169 | 0.3101 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 471 | -0.1968 | -0.3806 |
| seed_p | 471 | -0.3725 | -0.4491 |
| seed_p_vs_seed_pars | 437 | -0.4686 | -0.4830 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
