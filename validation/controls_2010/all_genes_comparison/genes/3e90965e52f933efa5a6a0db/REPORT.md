# YOL128C
Status: ok. Length: 1330 nt. Measured usable bases: 480. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 480 | 0.3118 | 0.3094 |
| rnafold | ok | 480 | 0.2509 | 0.2510 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 9 | undefined | undefined |
| seed_p | 9 | undefined | undefined |
| seed_p_vs_seed_pars | 4 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
