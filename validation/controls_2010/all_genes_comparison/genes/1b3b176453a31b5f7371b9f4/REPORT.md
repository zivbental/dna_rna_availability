# YPL162C
Status: ok. Length: 971 nt. Measured usable bases: 444. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 444 | 0.2796 | 0.2680 |
| rnafold | ok | 444 | 0.2625 | 0.2479 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 55 | -0.3372 | -0.5098 |
| seed_p | 55 | -0.5173 | -0.3550 |
| seed_p_vs_seed_pars | 40 | -0.4463 | -0.0714 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
