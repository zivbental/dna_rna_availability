# YIL088C
Status: ok. Length: 1591 nt. Measured usable bases: 1020. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1020 | 0.2581 | 0.2452 |
| rnafold | ok | 1020 | 0.2092 | 0.2187 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 442 | 0.0043 | -0.1720 |
| seed_p | 442 | 0.0604 | 0.0316 |
| seed_p_vs_seed_pars | 362 | -0.0226 | -0.0543 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
