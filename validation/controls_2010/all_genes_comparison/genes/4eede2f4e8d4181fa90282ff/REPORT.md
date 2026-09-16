# YDR408C
Status: ok. Length: 847 nt. Measured usable bases: 629. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 629 | 0.3797 | 0.3952 |
| rnafold | ok | 629 | 0.3384 | 0.3435 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 441 | -0.1160 | -0.3489 |
| seed_p | 441 | -0.1717 | -0.3753 |
| seed_p_vs_seed_pars | 354 | -0.3627 | -0.5025 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
