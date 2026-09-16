# YLR126C
Status: ok. Length: 880 nt. Measured usable bases: 309. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 309 | 0.4173 | 0.3961 |
| rnafold | ok | 309 | 0.3366 | 0.3375 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | 0.0081 | -0.0840 |
| seed_p | 66 | 0.3145 | 0.5355 |
| seed_p_vs_seed_pars | 50 | 0.2144 | 0.5133 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
