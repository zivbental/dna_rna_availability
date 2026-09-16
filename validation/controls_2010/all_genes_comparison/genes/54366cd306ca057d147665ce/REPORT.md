# YIL053W
Status: ok. Length: 931 nt. Measured usable bases: 811. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 811 | 0.3009 | 0.2884 |
| rnafold | ok | 811 | 0.2302 | 0.2302 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 743 | -0.2822 | -0.3174 |
| seed_p | 743 | -0.3794 | -0.3665 |
| seed_p_vs_seed_pars | 711 | -0.4527 | -0.4234 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
