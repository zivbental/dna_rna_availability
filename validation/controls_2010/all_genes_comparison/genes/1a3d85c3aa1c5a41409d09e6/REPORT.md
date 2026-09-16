# YGL211W
Status: ok. Length: 1209 nt. Measured usable bases: 615. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 615 | 0.3791 | 0.3577 |
| rnafold | ok | 615 | 0.3147 | 0.3084 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 136 | -0.1967 | -0.2495 |
| seed_p | 136 | -0.2838 | -0.3374 |
| seed_p_vs_seed_pars | 98 | -0.4149 | -0.5279 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
