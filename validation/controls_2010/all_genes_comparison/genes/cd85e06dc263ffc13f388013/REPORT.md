# YOR184W
Status: ok. Length: 1286 nt. Measured usable bases: 409. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 409 | 0.4372 | 0.4284 |
| rnafold | ok | 409 | 0.4212 | 0.4117 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 317 | -0.0585 | -0.0856 |
| seed_p | 317 | -0.1228 | -0.1521 |
| seed_p_vs_seed_pars | 234 | -0.4568 | -0.4396 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
