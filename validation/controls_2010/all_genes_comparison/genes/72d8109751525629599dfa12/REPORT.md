# YJR133W
Status: ok. Length: 827 nt. Measured usable bases: 526. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 526 | 0.4060 | 0.4001 |
| rnafold | ok | 526 | 0.3835 | 0.3793 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 208 | -0.0842 | -0.4015 |
| seed_p | 208 | -0.3757 | -0.3046 |
| seed_p_vs_seed_pars | 147 | -0.5225 | -0.3270 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
