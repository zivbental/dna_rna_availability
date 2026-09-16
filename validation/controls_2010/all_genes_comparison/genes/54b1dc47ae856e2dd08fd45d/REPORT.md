# YLL026W
Status: ok. Length: 2859 nt. Measured usable bases: 1945. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1945 | 0.3184 | 0.3138 |
| rnafold | ok | 1945 | 0.2770 | 0.2753 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1047 | 0.0065 | -0.0447 |
| seed_p | 1047 | -0.2382 | -0.1458 |
| seed_p_vs_seed_pars | 799 | -0.2919 | -0.1126 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
