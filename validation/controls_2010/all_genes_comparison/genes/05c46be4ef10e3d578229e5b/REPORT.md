# YHR063C
Status: ok. Length: 1214 nt. Measured usable bases: 796. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 796 | 0.3642 | 0.3462 |
| rnafold | ok | 796 | 0.2974 | 0.2847 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 402 | -0.1821 | -0.1239 |
| seed_p | 402 | -0.2133 | -0.3000 |
| seed_p_vs_seed_pars | 284 | -0.5205 | -0.4991 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
