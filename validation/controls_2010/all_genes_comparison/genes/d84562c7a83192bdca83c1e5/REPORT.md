# YIR037W
Status: ok. Length: 630 nt. Measured usable bases: 440. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 440 | 0.1724 | 0.1746 |
| rnafold | ok | 440 | 0.1240 | 0.1430 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 292 | 0.0091 | 0.0230 |
| seed_p | 292 | 0.0289 | 0.0868 |
| seed_p_vs_seed_pars | 268 | -0.1334 | -0.0505 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
