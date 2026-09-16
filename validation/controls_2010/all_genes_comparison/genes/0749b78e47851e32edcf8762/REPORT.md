# YHR161C
Status: ok. Length: 2310 nt. Measured usable bases: 867. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 867 | 0.2835 | 0.2660 |
| rnafold | ok | 867 | 0.2738 | 0.2608 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | -0.0981 | -0.4376 |
| seed_p | 37 | -0.8023 | -0.2029 |
| seed_p_vs_seed_pars | 22 | 0.3775 | 0.6382 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
