# YBR293W
Status: ok. Length: 2038 nt. Measured usable bases: 716. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 716 | 0.2804 | 0.2730 |
| rnafold | ok | 716 | 0.2434 | 0.2386 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 76 | -0.4010 | -0.3792 |
| seed_p | 76 | 0.1929 | 0.0945 |
| seed_p_vs_seed_pars | 48 | 0.3044 | 0.5363 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
