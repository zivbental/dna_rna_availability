# YLR421C
Status: ok. Length: 713 nt. Measured usable bases: 420. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 420 | 0.3556 | 0.3498 |
| rnafold | ok | 420 | 0.3221 | 0.3005 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 210 | -0.1264 | 0.0706 |
| seed_p | 210 | -0.1208 | -0.0241 |
| seed_p_vs_seed_pars | 176 | -0.0635 | 0.0194 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
