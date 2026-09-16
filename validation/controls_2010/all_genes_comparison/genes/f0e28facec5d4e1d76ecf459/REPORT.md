# YDR012W
Status: ok. Length: 1204 nt. Measured usable bases: 182. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 182 | 0.3466 | 0.3340 |
| rnafold | ok | 182 | 0.3062 | 0.2857 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | -0.6008 | -0.2384 |
| seed_p | 87 | -0.2242 | -0.0838 |
| seed_p_vs_seed_pars | 82 | -0.2603 | -0.1119 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
