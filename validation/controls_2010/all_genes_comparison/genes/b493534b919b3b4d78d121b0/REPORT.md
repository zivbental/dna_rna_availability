# YBL064C
Status: ok. Length: 868 nt. Measured usable bases: 495. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 495 | 0.3327 | 0.3457 |
| rnafold | ok | 495 | 0.3415 | 0.3495 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 211 | -0.1159 | -0.0038 |
| seed_p | 211 | -0.0831 | -0.2001 |
| seed_p_vs_seed_pars | 155 | -0.0176 | -0.2894 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
