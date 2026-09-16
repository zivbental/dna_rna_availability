# YLR192C
Status: ok. Length: 1074 nt. Measured usable bases: 771. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 771 | 0.3281 | 0.3275 |
| rnafold | ok | 771 | 0.2854 | 0.3123 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 563 | -0.2006 | -0.1847 |
| seed_p | 563 | -0.1747 | -0.1217 |
| seed_p_vs_seed_pars | 424 | -0.3186 | -0.3403 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
