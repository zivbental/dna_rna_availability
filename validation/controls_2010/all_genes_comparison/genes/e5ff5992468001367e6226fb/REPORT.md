# YKL077W
Status: ok. Length: 1490 nt. Measured usable bases: 1119. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1119 | 0.2460 | 0.2327 |
| rnafold | ok | 1119 | 0.1674 | 0.1742 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 794 | 0.0816 | -0.0035 |
| seed_p | 794 | -0.1306 | -0.0885 |
| seed_p_vs_seed_pars | 636 | -0.2847 | -0.2824 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
