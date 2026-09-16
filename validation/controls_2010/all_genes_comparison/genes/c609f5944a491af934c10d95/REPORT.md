# YLL010C
Status: ok. Length: 1759 nt. Measured usable bases: 828. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 828 | 0.1903 | 0.1887 |
| rnafold | ok | 828 | 0.1007 | 0.0956 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 182 | 0.3318 | 0.2225 |
| seed_p | 182 | 0.1638 | 0.1959 |
| seed_p_vs_seed_pars | 129 | -0.2451 | -0.2154 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
