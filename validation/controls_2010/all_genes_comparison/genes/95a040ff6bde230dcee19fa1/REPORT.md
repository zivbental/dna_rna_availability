# YDR238C
Status: ok. Length: 3230 nt. Measured usable bases: 2096. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2096 | 0.2929 | 0.2710 |
| rnafold | ok | 2096 | 0.2220 | 0.2216 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1131 | -0.0773 | -0.1665 |
| seed_p | 1131 | -0.1596 | -0.0927 |
| seed_p_vs_seed_pars | 923 | -0.2185 | -0.1110 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
