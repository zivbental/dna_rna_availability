# YML081W
Status: ok. Length: 3927 nt. Measured usable bases: 1494. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1494 | 0.2810 | 0.2665 |
| rnafold | ok | 1494 | 0.2229 | 0.2167 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 187 | -0.2831 | -0.2851 |
| seed_p | 187 | -0.4013 | -0.3366 |
| seed_p_vs_seed_pars | 131 | -0.7071 | -0.5339 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
