# YML079W
Status: ok. Length: 696 nt. Measured usable bases: 432. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 432 | 0.3299 | 0.3164 |
| rnafold | ok | 432 | 0.2065 | 0.2257 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 189 | 0.0907 | 0.0397 |
| seed_p | 189 | 0.1626 | 0.2479 |
| seed_p_vs_seed_pars | 138 | 0.1999 | 0.3738 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
