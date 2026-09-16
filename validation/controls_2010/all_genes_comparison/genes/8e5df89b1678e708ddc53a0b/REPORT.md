# YCL025C
Status: ok. Length: 2164 nt. Measured usable bases: 913. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 913 | 0.3150 | 0.2836 |
| rnafold | ok | 913 | 0.2326 | 0.2207 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 102 | 0.0233 | -0.1227 |
| seed_p | 102 | -0.0188 | 0.0197 |
| seed_p_vs_seed_pars | 65 | -0.1079 | -0.2316 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
