# YAR028W
Status: ok. Length: 950 nt. Measured usable bases: 468. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 468 | 0.3638 | 0.3444 |
| rnafold | ok | 468 | 0.3196 | 0.3212 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | -0.4782 | -0.6767 |
| seed_p | 62 | -0.8758 | -0.8941 |
| seed_p_vs_seed_pars | 47 | -0.8884 | -0.8648 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
