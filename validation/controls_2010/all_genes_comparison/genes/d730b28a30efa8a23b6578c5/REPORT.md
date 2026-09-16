# YOL142W
Status: ok. Length: 797 nt. Measured usable bases: 449. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 449 | 0.3106 | 0.2895 |
| rnafold | ok | 449 | 0.2793 | 0.2839 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | 0.0684 | 0.0039 |
| seed_p | 135 | -0.5781 | -0.3014 |
| seed_p_vs_seed_pars | 102 | -0.7098 | -0.5038 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
