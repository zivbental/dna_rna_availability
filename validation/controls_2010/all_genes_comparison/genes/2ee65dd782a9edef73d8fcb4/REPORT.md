# YKR051W
Status: ok. Length: 1706 nt. Measured usable bases: 522. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 522 | 0.3035 | 0.2899 |
| rnafold | ok | 522 | 0.2859 | 0.2748 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 48 | -0.4346 | -0.6231 |
| seed_p | 48 | -0.6644 | -0.7184 |
| seed_p_vs_seed_pars | 38 | -0.7769 | -0.8258 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
