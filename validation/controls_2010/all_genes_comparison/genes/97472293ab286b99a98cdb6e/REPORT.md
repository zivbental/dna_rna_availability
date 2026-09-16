# YBL006C
Status: ok. Length: 716 nt. Measured usable bases: 485. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 485 | 0.4627 | 0.4651 |
| rnafold | ok | 485 | 0.4206 | 0.4464 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 257 | -0.3909 | -0.3978 |
| seed_p | 257 | -0.3134 | -0.3157 |
| seed_p_vs_seed_pars | 211 | -0.3014 | -0.2767 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
