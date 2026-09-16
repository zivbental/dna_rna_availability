# YDR189W
Status: ok. Length: 2135 nt. Measured usable bases: 1189. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1189 | 0.3575 | 0.3308 |
| rnafold | ok | 1189 | 0.3057 | 0.2813 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 319 | 0.0375 | -0.0641 |
| seed_p | 319 | -0.1291 | -0.0146 |
| seed_p_vs_seed_pars | 192 | -0.3322 | -0.2287 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
