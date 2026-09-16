# YIL016W
Status: ok. Length: 524 nt. Measured usable bases: 329. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 329 | 0.2915 | 0.3154 |
| rnafold | ok | 329 | 0.2842 | 0.3010 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 178 | -0.1455 | -0.3359 |
| seed_p | 178 | -0.1198 | -0.1818 |
| seed_p_vs_seed_pars | 162 | -0.1943 | -0.2876 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
