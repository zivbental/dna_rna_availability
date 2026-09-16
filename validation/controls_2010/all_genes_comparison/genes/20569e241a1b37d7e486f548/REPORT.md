# YEL031W
Status: ok. Length: 3759 nt. Measured usable bases: 2909. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2909 | 0.2866 | 0.2649 |
| rnafold | ok | 2909 | 0.2410 | 0.2373 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2253 | -0.0888 | -0.1100 |
| seed_p | 2253 | -0.1690 | -0.1461 |
| seed_p_vs_seed_pars | 1821 | -0.2834 | -0.2097 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
