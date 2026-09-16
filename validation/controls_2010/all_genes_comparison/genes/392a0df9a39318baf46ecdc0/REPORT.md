# YGR081C
Status: ok. Length: 709 nt. Measured usable bases: 283. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 283 | 0.3060 | 0.3039 |
| rnafold | ok | 283 | 0.3669 | 0.3520 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 30 | -0.5580 | -0.8759 |
| seed_p | 30 | -0.3328 | -0.2367 |
| seed_p_vs_seed_pars | 23 | -0.4922 | -0.6246 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
