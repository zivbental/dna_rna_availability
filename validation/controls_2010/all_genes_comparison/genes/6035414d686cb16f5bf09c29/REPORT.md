# YNL315C
Status: ok. Length: 1023 nt. Measured usable bases: 613. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 613 | 0.4027 | 0.3833 |
| rnafold | ok | 613 | 0.2981 | 0.2799 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 268 | -0.1981 | -0.3924 |
| seed_p | 268 | -0.3329 | -0.3521 |
| seed_p_vs_seed_pars | 220 | -0.4267 | -0.4169 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
