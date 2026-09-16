# YHL039W
Status: ok. Length: 1758 nt. Measured usable bases: 893. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 893 | 0.2992 | 0.2770 |
| rnafold | ok | 893 | 0.2867 | 0.2757 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 212 | -0.0862 | -0.2976 |
| seed_p | 212 | -0.1715 | -0.1865 |
| seed_p_vs_seed_pars | 163 | -0.1092 | -0.0735 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
