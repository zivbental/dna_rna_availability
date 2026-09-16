# YML081C-A
Status: ok. Length: 364 nt. Measured usable bases: 275. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 275 | 0.3093 | 0.3225 |
| rnafold | ok | 275 | 0.2886 | 0.2952 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 263 | -0.1370 | -0.3566 |
| seed_p | 263 | -0.0993 | -0.2083 |
| seed_p_vs_seed_pars | 192 | -0.0332 | -0.1382 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
