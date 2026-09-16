# YGL025C
Status: ok. Length: 1258 nt. Measured usable bases: 588. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 588 | 0.3129 | 0.3115 |
| rnafold | ok | 588 | 0.2656 | 0.2852 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 108 | -0.3801 | -0.4746 |
| seed_p | 108 | -0.7144 | -0.6380 |
| seed_p_vs_seed_pars | 98 | -0.5906 | -0.6321 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
