# YDR481C
Status: ok. Length: 1787 nt. Measured usable bases: 1410. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1410 | 0.3560 | 0.3308 |
| rnafold | ok | 1410 | 0.2933 | 0.2826 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1125 | -0.1207 | -0.2551 |
| seed_p | 1125 | -0.2039 | -0.2547 |
| seed_p_vs_seed_pars | 948 | -0.3103 | -0.3589 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
