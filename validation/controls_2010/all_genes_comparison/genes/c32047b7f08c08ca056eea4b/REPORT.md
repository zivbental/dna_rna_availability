# YKL056C
Status: ok. Length: 765 nt. Measured usable bases: 689. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 689 | 0.3900 | 0.3811 |
| rnafold | ok | 689 | 0.2726 | 0.2666 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 663 | -0.0338 | -0.1760 |
| seed_p | 663 | -0.0988 | -0.1825 |
| seed_p_vs_seed_pars | 632 | -0.1919 | -0.2809 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
