# YNL040W
Status: ok. Length: 1567 nt. Measured usable bases: 677. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 677 | 0.3385 | 0.3333 |
| rnafold | ok | 677 | 0.2927 | 0.2999 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 50 | -0.4309 | -0.5026 |
| seed_p | 50 | -0.5681 | -0.5923 |
| seed_p_vs_seed_pars | 45 | -0.6757 | -0.6024 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
