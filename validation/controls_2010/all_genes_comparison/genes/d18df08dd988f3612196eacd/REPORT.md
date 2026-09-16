# YDR398W
Status: ok. Length: 2186 nt. Measured usable bases: 1197. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1197 | 0.3338 | 0.3312 |
| rnafold | ok | 1197 | 0.2764 | 0.2860 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 357 | -0.2184 | -0.2648 |
| seed_p | 357 | -0.2220 | -0.2316 |
| seed_p_vs_seed_pars | 262 | -0.2138 | -0.1776 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
