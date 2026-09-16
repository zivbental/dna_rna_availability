# YNL259C
Status: ok. Length: 323 nt. Measured usable bases: 163. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 163 | 0.2312 | 0.2042 |
| rnafold | ok | 163 | 0.1095 | 0.1269 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 40 | -0.7318 | -0.6556 |
| seed_p | 40 | -0.8071 | -0.7334 |
| seed_p_vs_seed_pars | 22 | -0.3212 | -0.7493 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
