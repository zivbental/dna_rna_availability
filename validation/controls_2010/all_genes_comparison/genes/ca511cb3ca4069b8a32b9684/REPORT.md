# YLR129W
Status: ok. Length: 3042 nt. Measured usable bases: 1402. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1402 | 0.3148 | 0.2997 |
| rnafold | ok | 1402 | 0.2786 | 0.2744 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 229 | -0.1953 | -0.2966 |
| seed_p | 229 | -0.2133 | -0.0804 |
| seed_p_vs_seed_pars | 176 | -0.3258 | -0.1289 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
