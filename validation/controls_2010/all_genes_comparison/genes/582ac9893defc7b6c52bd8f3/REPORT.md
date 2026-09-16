# YJL172W
Status: ok. Length: 1898 nt. Measured usable bases: 1417. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1417 | 0.3147 | 0.2868 |
| rnafold | ok | 1417 | 0.2247 | 0.2159 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1155 | 0.0336 | -0.0263 |
| seed_p | 1155 | -0.0927 | -0.0254 |
| seed_p_vs_seed_pars | 934 | -0.1815 | -0.1197 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
