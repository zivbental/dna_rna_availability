# YEL048C
Status: ok. Length: 1031 nt. Measured usable bases: 576. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 576 | 0.2659 | 0.2353 |
| rnafold | ok | 576 | 0.2798 | 0.2647 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 165 | -0.4446 | -0.3001 |
| seed_p | 165 | -0.4667 | -0.2963 |
| seed_p_vs_seed_pars | 127 | -0.4456 | -0.2435 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
