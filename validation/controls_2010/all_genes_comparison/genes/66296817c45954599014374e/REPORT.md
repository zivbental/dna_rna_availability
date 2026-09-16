# YNL251C
Status: ok. Length: 2041 nt. Measured usable bases: 1068. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1068 | 0.2258 | 0.2030 |
| rnafold | ok | 1068 | 0.1815 | 0.1663 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 209 | -0.0119 | -0.0067 |
| seed_p | 209 | -0.2328 | -0.1238 |
| seed_p_vs_seed_pars | 136 | -0.1411 | -0.1625 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
