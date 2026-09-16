# YAL014C
Status: ok. Length: 950 nt. Measured usable bases: 567.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 567 | 0.2905 | 0.2693 |
| rnafold | ok | 567 | 0.2346 | 0.2161 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 320 | 0.1472 | 0.2313 |
| seed_p | 320 | -0.2406 | -0.1687 |
| seed_p_vs_seed_pars | 250 | -0.2766 | -0.1864 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
