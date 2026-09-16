# YBR207W
Status: ok. Length: 1550 nt. Measured usable bases: 780. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 780 | 0.3252 | 0.3208 |
| rnafold | ok | 780 | 0.2743 | 0.2610 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 264 | -0.3317 | -0.1271 |
| seed_p | 264 | -0.6007 | -0.2362 |
| seed_p_vs_seed_pars | 211 | -0.5512 | -0.3527 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
