# YNL067W
Status: ok. Length: 777 nt. Measured usable bases: 435. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 435 | 0.3111 | 0.3151 |
| rnafold | ok | 435 | 0.2629 | 0.3181 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 301 | 0.0815 | 0.0766 |
| seed_p | 301 | -0.0337 | -0.1228 |
| seed_p_vs_seed_pars | 258 | -0.0241 | -0.2081 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
