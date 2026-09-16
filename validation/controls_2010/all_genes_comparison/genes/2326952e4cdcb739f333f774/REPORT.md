# YKL007W
Status: ok. Length: 967 nt. Measured usable bases: 543. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 543 | 0.3544 | 0.3325 |
| rnafold | ok | 543 | 0.2973 | 0.2704 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 286 | -0.1758 | -0.1933 |
| seed_p | 286 | -0.5176 | -0.5010 |
| seed_p_vs_seed_pars | 216 | -0.4348 | -0.5375 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
