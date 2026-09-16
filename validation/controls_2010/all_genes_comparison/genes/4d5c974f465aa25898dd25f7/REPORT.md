# YLR194C
Status: ok. Length: 949 nt. Measured usable bases: 530. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 530 | 0.2890 | 0.2836 |
| rnafold | ok | 530 | 0.3119 | 0.3047 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 211 | 0.0923 | 0.0516 |
| seed_p | 211 | 0.1447 | 0.1893 |
| seed_p_vs_seed_pars | 181 | 0.1138 | 0.1018 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
