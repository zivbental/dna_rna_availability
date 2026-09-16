# YGR284C
Status: ok. Length: 1137 nt. Measured usable bases: 865. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 865 | 0.3288 | 0.3295 |
| rnafold | ok | 865 | 0.2707 | 0.2825 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 643 | -0.3535 | -0.1692 |
| seed_p | 643 | -0.2014 | -0.0181 |
| seed_p_vs_seed_pars | 502 | -0.1732 | -0.0677 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
