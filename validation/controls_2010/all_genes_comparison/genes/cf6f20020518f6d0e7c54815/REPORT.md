# YKL138C-A
Status: ok. Length: 291 nt. Measured usable bases: 116. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 116 | 0.4013 | 0.4130 |
| rnafold | ok | 116 | 0.3634 | 0.3747 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 20 | -0.6777 | -0.6526 |
| seed_p | 20 | 0.2396 | 0.6405 |
| seed_p_vs_seed_pars | 12 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
