# YDR345C
Status: ok. Length: 1924 nt. Measured usable bases: 1177. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1177 | 0.3415 | 0.3424 |
| rnafold | ok | 1177 | 0.2154 | 0.2139 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 997 | -0.2148 | -0.1954 |
| seed_p | 997 | -0.3098 | -0.2994 |
| seed_p_vs_seed_pars | 857 | -0.2770 | -0.2875 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
