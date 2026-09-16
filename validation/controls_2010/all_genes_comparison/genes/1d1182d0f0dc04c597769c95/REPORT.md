# YFR002W
Status: ok. Length: 2619 nt. Measured usable bases: 1048. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1048 | 0.3354 | 0.3202 |
| rnafold | ok | 1048 | 0.3021 | 0.2936 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | 0.2680 | -0.2213 |
| seed_p | 65 | -0.0732 | -0.0958 |
| seed_p_vs_seed_pars | 37 | 0.1852 | 0.0288 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
