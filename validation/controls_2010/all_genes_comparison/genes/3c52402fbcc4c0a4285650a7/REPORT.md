# YGR286C
Status: ok. Length: 1533 nt. Measured usable bases: 702. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 702 | 0.3899 | 0.3745 |
| rnafold | ok | 702 | 0.2980 | 0.3035 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 167 | -0.2261 | -0.4470 |
| seed_p | 167 | -0.3412 | -0.4592 |
| seed_p_vs_seed_pars | 126 | -0.2240 | -0.4317 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
