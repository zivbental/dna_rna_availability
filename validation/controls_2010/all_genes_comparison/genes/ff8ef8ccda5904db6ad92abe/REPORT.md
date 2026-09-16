# YLL058W
Status: ok. Length: 1848 nt. Measured usable bases: 667. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 667 | 0.3927 | 0.3847 |
| rnafold | ok | 667 | 0.2689 | 0.2648 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 22 | -0.4753 | 0.0707 |
| seed_p | 22 | 0.1444 | -0.1269 |
| seed_p_vs_seed_pars | 11 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
