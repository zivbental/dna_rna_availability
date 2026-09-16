# YGL011C
Status: ok. Length: 879 nt. Measured usable bases: 700. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 700 | 0.3098 | 0.2872 |
| rnafold | ok | 700 | 0.2591 | 0.2629 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 601 | -0.1057 | 0.0008 |
| seed_p | 601 | -0.1081 | -0.0960 |
| seed_p_vs_seed_pars | 449 | -0.2123 | -0.1396 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
