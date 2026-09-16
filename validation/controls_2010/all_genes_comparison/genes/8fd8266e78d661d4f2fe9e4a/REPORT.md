# YGL223C
Status: ok. Length: 1319 nt. Measured usable bases: 591. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 591 | 0.2091 | 0.2126 |
| rnafold | ok | 591 | 0.2004 | 0.2114 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | -0.0648 | -0.0196 |
| seed_p | 66 | -0.0410 | 0.2707 |
| seed_p_vs_seed_pars | 30 | 0.7638 | 0.6661 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
