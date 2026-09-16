# YPL204W
Status: ok. Length: 1830 nt. Measured usable bases: 884. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 884 | 0.2873 | 0.2777 |
| rnafold | ok | 884 | 0.2905 | 0.2859 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 257 | -0.1883 | -0.3119 |
| seed_p | 257 | -0.1054 | -0.2636 |
| seed_p_vs_seed_pars | 169 | -0.0789 | -0.2343 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
