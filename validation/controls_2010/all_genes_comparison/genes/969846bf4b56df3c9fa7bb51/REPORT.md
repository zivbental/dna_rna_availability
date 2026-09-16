# YCR002C
Status: ok. Length: 1042 nt. Measured usable bases: 681. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 681 | 0.2463 | 0.2483 |
| rnafold | ok | 681 | 0.2346 | 0.2291 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 311 | -0.0511 | -0.2839 |
| seed_p | 311 | -0.2572 | -0.2575 |
| seed_p_vs_seed_pars | 203 | -0.1442 | -0.1478 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
