# YNL080C
Status: ok. Length: 1269 nt. Measured usable bases: 698. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 698 | 0.2339 | 0.2273 |
| rnafold | ok | 698 | 0.2346 | 0.1965 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 223 | 0.0867 | -0.0643 |
| seed_p | 223 | -0.1729 | -0.1140 |
| seed_p_vs_seed_pars | 174 | -0.4224 | -0.3571 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
