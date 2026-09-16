# YDR237W
Status: ok. Length: 1142 nt. Measured usable bases: 563. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 563 | 0.3759 | 0.3490 |
| rnafold | ok | 563 | 0.2685 | 0.2592 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 81 | 0.3577 | 0.1825 |
| seed_p | 81 | -0.1200 | 0.0290 |
| seed_p_vs_seed_pars | 54 | 0.1010 | 0.3193 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
