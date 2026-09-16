# YNL035C
Status: ok. Length: 1422 nt. Measured usable bases: 790. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 790 | 0.3308 | 0.3226 |
| rnafold | ok | 790 | 0.2890 | 0.2873 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 200 | -0.2310 | -0.1385 |
| seed_p | 200 | -0.1858 | -0.2155 |
| seed_p_vs_seed_pars | 143 | -0.0263 | -0.1006 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
