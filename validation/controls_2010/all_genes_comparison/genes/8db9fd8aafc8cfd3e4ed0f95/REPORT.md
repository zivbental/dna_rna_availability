# YLR221C
Status: ok. Length: 913 nt. Measured usable bases: 413. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 413 | 0.2956 | 0.3035 |
| rnafold | ok | 413 | 0.2789 | 0.2783 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 40 | -0.5144 | -0.4513 |
| seed_p | 40 | -0.4737 | -0.5387 |
| seed_p_vs_seed_pars | 22 | -0.7266 | -0.8942 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
