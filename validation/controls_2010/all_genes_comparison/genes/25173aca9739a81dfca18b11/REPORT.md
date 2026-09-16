# YMR252C
Status: ok. Length: 774 nt. Measured usable bases: 247. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 247 | 0.2558 | 0.2470 |
| rnafold | ok | 247 | 0.2315 | 0.2331 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 64 | -0.1383 | -0.3334 |
| seed_p | 64 | -0.5905 | -0.3902 |
| seed_p_vs_seed_pars | 60 | -0.9048 | -0.5351 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
