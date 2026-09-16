# YLR399C
Status: ok. Length: 2271 nt. Measured usable bases: 1107. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1107 | 0.2994 | 0.2919 |
| rnafold | ok | 1107 | 0.2890 | 0.2783 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 230 | 0.3371 | 0.2854 |
| seed_p | 230 | 0.2257 | 0.2510 |
| seed_p_vs_seed_pars | 157 | 0.0102 | -0.0393 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
