# YML031W
Status: ok. Length: 2034 nt. Measured usable bases: 1273. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1273 | 0.2605 | 0.2475 |
| rnafold | ok | 1273 | 0.1899 | 0.1766 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 592 | 0.0444 | -0.0238 |
| seed_p | 592 | 0.0682 | 0.0403 |
| seed_p_vs_seed_pars | 448 | -0.0726 | -0.0974 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
