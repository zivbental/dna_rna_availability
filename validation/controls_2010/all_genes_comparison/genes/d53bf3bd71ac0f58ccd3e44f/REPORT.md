# YDR231C
Status: ok. Length: 791 nt. Measured usable bases: 372. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 372 | 0.3720 | 0.3720 |
| rnafold | ok | 372 | 0.4292 | 0.4292 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 100 | -0.0402 | -0.3430 |
| seed_p | 100 | -0.4149 | -0.5053 |
| seed_p_vs_seed_pars | 77 | -0.4279 | -0.6369 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
