# YIL145C
Status: ok. Length: 1305 nt. Measured usable bases: 910. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 910 | 0.3917 | 0.3626 |
| rnafold | ok | 910 | 0.3189 | 0.3002 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 524 | -0.0280 | -0.1785 |
| seed_p | 524 | -0.1200 | -0.0967 |
| seed_p_vs_seed_pars | 450 | -0.3166 | -0.3323 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
