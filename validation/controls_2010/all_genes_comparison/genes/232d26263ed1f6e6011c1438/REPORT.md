# YBR071W
Status: ok. Length: 957 nt. Measured usable bases: 418. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 418 | 0.2723 | 0.2596 |
| rnafold | ok | 418 | 0.2224 | 0.2163 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 124 | 0.0115 | -0.3784 |
| seed_p | 124 | -0.2694 | -0.2467 |
| seed_p_vs_seed_pars | 104 | -0.4406 | -0.2725 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
