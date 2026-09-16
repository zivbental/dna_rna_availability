# YCR065W
Status: ok. Length: 1819 nt. Measured usable bases: 982. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 982 | 0.2905 | 0.2796 |
| rnafold | ok | 982 | 0.2382 | 0.2270 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 277 | -0.1029 | -0.1104 |
| seed_p | 277 | -0.1730 | -0.2606 |
| seed_p_vs_seed_pars | 220 | -0.3252 | -0.4836 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
