# YOL036W
Status: ok. Length: 2815 nt. Measured usable bases: 1102. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1102 | 0.2172 | 0.2108 |
| rnafold | ok | 1102 | 0.2249 | 0.2235 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 94 | -0.5892 | -0.1725 |
| seed_p | 94 | -0.6075 | -0.3905 |
| seed_p_vs_seed_pars | 56 | -0.6797 | -0.5755 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
