# YOR131C
Status: ok. Length: 855 nt. Measured usable bases: 364. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 364 | 0.3815 | 0.3491 |
| rnafold | ok | 364 | 0.2848 | 0.2461 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 112 | -0.0170 | -0.0262 |
| seed_p | 112 | -0.4461 | -0.2528 |
| seed_p_vs_seed_pars | 82 | -0.0680 | -0.0204 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
