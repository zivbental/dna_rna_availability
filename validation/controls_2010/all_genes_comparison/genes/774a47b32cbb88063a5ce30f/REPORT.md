# YGR220C
Status: ok. Length: 922 nt. Measured usable bases: 471. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 471 | 0.3914 | 0.3785 |
| rnafold | ok | 471 | 0.3455 | 0.3260 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 186 | 0.2335 | 0.2539 |
| seed_p | 186 | -0.1983 | -0.1776 |
| seed_p_vs_seed_pars | 137 | -0.5917 | -0.4297 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
