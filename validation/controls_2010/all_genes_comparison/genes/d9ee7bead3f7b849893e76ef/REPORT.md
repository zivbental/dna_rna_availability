# YJR046W
Status: ok. Length: 1894 nt. Measured usable bases: 1007. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1007 | 0.3360 | 0.3226 |
| rnafold | ok | 1007 | 0.2895 | 0.2680 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 225 | -0.2908 | -0.4696 |
| seed_p | 225 | -0.2233 | -0.1426 |
| seed_p_vs_seed_pars | 172 | -0.0941 | 0.0924 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
