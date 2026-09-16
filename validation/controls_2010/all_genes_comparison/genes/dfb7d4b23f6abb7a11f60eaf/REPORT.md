# YLR347C
Status: ok. Length: 2981 nt. Measured usable bases: 1905. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1905 | 0.3261 | 0.3184 |
| rnafold | ok | 1905 | 0.2571 | 0.2473 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 842 | -0.1207 | -0.2271 |
| seed_p | 842 | -0.2716 | -0.1889 |
| seed_p_vs_seed_pars | 687 | -0.5195 | -0.4151 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
