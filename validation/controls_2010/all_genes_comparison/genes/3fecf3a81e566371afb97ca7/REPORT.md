# YML069W
Status: ok. Length: 1802 nt. Measured usable bases: 883. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 883 | 0.3173 | 0.3160 |
| rnafold | ok | 883 | 0.3120 | 0.3089 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 163 | 0.4354 | 0.2473 |
| seed_p | 163 | -0.2118 | 0.0076 |
| seed_p_vs_seed_pars | 118 | -0.5544 | -0.2272 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
