# YDR280W
Status: ok. Length: 1177 nt. Measured usable bases: 584. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 584 | 0.4017 | 0.3849 |
| rnafold | ok | 584 | 0.3299 | 0.3030 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 97 | -0.1375 | -0.0680 |
| seed_p | 97 | -0.0657 | -0.1571 |
| seed_p_vs_seed_pars | 71 | -0.5346 | -0.4636 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
