# YGR266W
Status: ok. Length: 2403 nt. Measured usable bases: 974. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 974 | 0.3756 | 0.3680 |
| rnafold | ok | 974 | 0.3033 | 0.2966 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | -0.2026 | -0.4015 |
| seed_p | 77 | 0.4646 | 0.3360 |
| seed_p_vs_seed_pars | 67 | 0.1568 | 0.1693 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
