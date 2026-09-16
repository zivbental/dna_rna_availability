# YMR202W
Status: ok. Length: 768 nt. Measured usable bases: 709. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 709 | 0.3646 | 0.3514 |
| rnafold | ok | 709 | 0.3138 | 0.3002 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 701 | -0.3130 | -0.3420 |
| seed_p | 701 | -0.4691 | -0.4549 |
| seed_p_vs_seed_pars | 662 | -0.4355 | -0.4935 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
