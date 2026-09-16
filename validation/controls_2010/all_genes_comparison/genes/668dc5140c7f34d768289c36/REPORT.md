# YNL132W
Status: ok. Length: 3335 nt. Measured usable bases: 1742. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1742 | 0.3078 | 0.3004 |
| rnafold | ok | 1742 | 0.2643 | 0.2554 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 374 | 0.0885 | -0.0463 |
| seed_p | 374 | -0.4479 | -0.2898 |
| seed_p_vs_seed_pars | 231 | -0.6175 | -0.4782 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
