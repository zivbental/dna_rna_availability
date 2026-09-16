# YBR211C
Status: ok. Length: 1166 nt. Measured usable bases: 348. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 348 | 0.3385 | 0.3460 |
| rnafold | ok | 348 | 0.2716 | 0.2760 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 36 | -0.4395 | -0.6436 |
| seed_p | 36 | 0.2200 | -0.1477 |
| seed_p_vs_seed_pars | 26 | 0.2475 | -0.1868 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
