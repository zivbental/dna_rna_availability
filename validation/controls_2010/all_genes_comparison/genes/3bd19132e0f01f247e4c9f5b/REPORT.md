# YNL284C
Status: ok. Length: 969 nt. Measured usable bases: 439. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 439 | 0.3759 | 0.3782 |
| rnafold | ok | 439 | 0.3710 | 0.3887 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 68 | 0.0575 | -0.0943 |
| seed_p | 68 | -0.4137 | -0.4599 |
| seed_p_vs_seed_pars | 39 | -0.1911 | -0.1929 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
