# YDR503C
Status: ok. Length: 1006 nt. Measured usable bases: 495. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 495 | 0.3077 | 0.2642 |
| rnafold | ok | 495 | 0.2871 | 0.2336 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.0817 | 0.0756 |
| seed_p | 67 | 0.1137 | 0.0729 |
| seed_p_vs_seed_pars | 30 | -0.6796 | -0.4458 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
