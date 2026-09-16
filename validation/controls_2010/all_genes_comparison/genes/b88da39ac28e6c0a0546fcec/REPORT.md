# YLR265C
Status: ok. Length: 1149 nt. Measured usable bases: 406. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 406 | 0.2874 | 0.2887 |
| rnafold | ok | 406 | 0.2172 | 0.2212 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | -0.0887 | -0.2803 |
| seed_p | 54 | 0.0160 | -0.0735 |
| seed_p_vs_seed_pars | 36 | -0.0397 | -0.0188 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
