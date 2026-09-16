# YGR180C
Status: ok. Length: 1314 nt. Measured usable bases: 1084. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1084 | 0.2529 | 0.2471 |
| rnafold | ok | 1084 | 0.1913 | 0.1844 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 995 | -0.0341 | -0.1166 |
| seed_p | 995 | -0.0350 | -0.0324 |
| seed_p_vs_seed_pars | 891 | -0.2056 | -0.1166 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
