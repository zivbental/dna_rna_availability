# YLR351C
Status: ok. Length: 994 nt. Measured usable bases: 624. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 624 | 0.3303 | 0.3113 |
| rnafold | ok | 624 | 0.3413 | 0.3353 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 374 | -0.1330 | 0.0229 |
| seed_p | 374 | -0.2276 | -0.1886 |
| seed_p_vs_seed_pars | 302 | -0.3929 | -0.3117 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
