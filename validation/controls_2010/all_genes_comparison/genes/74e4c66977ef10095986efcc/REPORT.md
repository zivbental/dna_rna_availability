# YKL094W
Status: ok. Length: 1057 nt. Measured usable bases: 724. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 724 | 0.3645 | 0.3585 |
| rnafold | ok | 724 | 0.3359 | 0.3360 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 369 | -0.0985 | -0.2469 |
| seed_p | 369 | -0.3725 | -0.3199 |
| seed_p_vs_seed_pars | 266 | -0.4468 | -0.3900 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
