# YMR126C
Status: ok. Length: 1194 nt. Measured usable bases: 500. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 500 | 0.2824 | 0.2727 |
| rnafold | ok | 500 | 0.2273 | 0.2290 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | 0.2675 | 0.3166 |
| seed_p | 54 | 0.3587 | 0.1842 |
| seed_p_vs_seed_pars | 32 | 0.4435 | -0.0202 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
