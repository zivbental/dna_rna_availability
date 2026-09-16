# YOL041C
Status: ok. Length: 1511 nt. Measured usable bases: 608. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 608 | 0.3452 | 0.3263 |
| rnafold | ok | 608 | 0.2081 | 0.1844 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 42 | -0.5678 | -0.5918 |
| seed_p | 42 | -0.8195 | -0.8118 |
| seed_p_vs_seed_pars | 35 | -0.9021 | -0.7848 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
