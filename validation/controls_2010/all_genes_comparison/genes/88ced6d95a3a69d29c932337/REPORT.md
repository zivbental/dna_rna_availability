# YGR024C
Status: ok. Length: 813 nt. Measured usable bases: 518. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 518 | 0.2817 | 0.2562 |
| rnafold | ok | 518 | 0.2640 | 0.2595 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 285 | -0.2825 | -0.2559 |
| seed_p | 285 | -0.5073 | -0.4323 |
| seed_p_vs_seed_pars | 234 | -0.4696 | -0.4818 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
