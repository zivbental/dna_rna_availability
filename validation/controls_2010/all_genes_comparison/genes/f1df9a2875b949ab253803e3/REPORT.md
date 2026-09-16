# YLR390W
Status: ok. Length: 615 nt. Measured usable bases: 228. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 228 | 0.3446 | 0.3636 |
| rnafold | ok | 228 | 0.3429 | 0.3554 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.3648 | -0.4095 |
| seed_p | 43 | -0.9383 | -0.9103 |
| seed_p_vs_seed_pars | 41 | -0.9229 | -0.9122 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
