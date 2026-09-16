# YGL056C
Status: ok. Length: 1748 nt. Measured usable bases: 782. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 782 | 0.3086 | 0.2891 |
| rnafold | ok | 782 | 0.3161 | 0.2822 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.2291 | -0.0269 |
| seed_p | 57 | -0.1980 | -0.0435 |
| seed_p_vs_seed_pars | 19 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
