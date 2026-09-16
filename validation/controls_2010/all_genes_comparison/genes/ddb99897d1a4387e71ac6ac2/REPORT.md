# YHL015W
Status: ok. Length: 686 nt. Measured usable bases: 603. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 603 | 0.3628 | 0.3662 |
| rnafold | ok | 603 | 0.3308 | 0.3358 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 571 | -0.1166 | -0.2475 |
| seed_p | 571 | -0.2271 | -0.1621 |
| seed_p_vs_seed_pars | 560 | -0.3162 | -0.2085 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
