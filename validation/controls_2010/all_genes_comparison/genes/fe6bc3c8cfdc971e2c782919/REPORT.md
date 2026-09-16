# YOR081C
Status: ok. Length: 2362 nt. Measured usable bases: 919. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 919 | 0.3008 | 0.3026 |
| rnafold | ok | 919 | 0.2264 | 0.2232 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 88 | -0.2393 | -0.3708 |
| seed_p | 88 | -0.2835 | -0.4871 |
| seed_p_vs_seed_pars | 53 | -0.7681 | -0.6604 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
