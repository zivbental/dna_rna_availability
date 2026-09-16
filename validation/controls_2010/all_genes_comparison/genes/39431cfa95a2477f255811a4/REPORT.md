# YEL034W
Status: ok. Length: 693 nt. Measured usable bases: 474. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 474 | 0.3337 | 0.3394 |
| rnafold | ok | 474 | 0.3147 | 0.2866 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 313 | -0.4834 | -0.4592 |
| seed_p | 313 | -0.5253 | -0.5338 |
| seed_p_vs_seed_pars | 292 | -0.4063 | -0.4083 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
