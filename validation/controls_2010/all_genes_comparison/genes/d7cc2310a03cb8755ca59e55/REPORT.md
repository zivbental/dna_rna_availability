# YBR005W
Status: ok. Length: 823 nt. Measured usable bases: 324. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 324 | 0.3566 | 0.3520 |
| rnafold | ok | 324 | 0.3599 | 0.3788 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 22 | -0.2354 | -0.6198 |
| seed_p | 22 | -0.7860 | -0.7826 |
| seed_p_vs_seed_pars | 16 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
