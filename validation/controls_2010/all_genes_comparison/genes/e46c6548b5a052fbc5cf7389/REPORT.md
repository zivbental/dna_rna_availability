# YCL036W
Status: ok. Length: 1790 nt. Measured usable bases: 896. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 896 | 0.3955 | 0.3970 |
| rnafold | ok | 896 | 0.3007 | 0.3236 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 181 | 0.0887 | 0.1182 |
| seed_p | 181 | 0.0189 | -0.0010 |
| seed_p_vs_seed_pars | 113 | -0.2981 | -0.3890 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
