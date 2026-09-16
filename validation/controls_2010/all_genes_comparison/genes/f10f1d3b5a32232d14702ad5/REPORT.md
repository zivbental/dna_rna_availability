# YDL185W
Status: ok. Length: 3346 nt. Measured usable bases: 2857. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2857 | 0.3095 | 0.2815 |
| rnafold | ok | 2857 | 0.2271 | 0.2200 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2655 | -0.0851 | -0.0547 |
| seed_p | 2655 | -0.3147 | -0.2119 |
| seed_p_vs_seed_pars | 2267 | -0.4230 | -0.3097 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
