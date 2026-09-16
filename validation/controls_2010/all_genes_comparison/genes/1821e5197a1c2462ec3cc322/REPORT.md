# YCL033C
Status: ok. Length: 585 nt. Measured usable bases: 271. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 271 | 0.3854 | 0.3614 |
| rnafold | ok | 271 | 0.3137 | 0.2961 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 130 | -0.3920 | -0.0951 |
| seed_p | 130 | -0.6920 | -0.6282 |
| seed_p_vs_seed_pars | 106 | -0.2838 | -0.2274 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
