# YGR231C
Status: ok. Length: 1156 nt. Measured usable bases: 717. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 717 | 0.3839 | 0.3679 |
| rnafold | ok | 717 | 0.3789 | 0.3631 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 402 | -0.0908 | -0.1761 |
| seed_p | 402 | -0.2568 | -0.1501 |
| seed_p_vs_seed_pars | 308 | -0.5645 | -0.4405 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
