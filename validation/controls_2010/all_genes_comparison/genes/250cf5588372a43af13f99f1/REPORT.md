# YKL096W
Status: ok. Length: 866 nt. Measured usable bases: 692. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 692 | 0.2793 | 0.2740 |
| rnafold | ok | 692 | 0.2276 | 0.2208 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 625 | -0.3528 | -0.1618 |
| seed_p | 625 | -0.3886 | -0.2987 |
| seed_p_vs_seed_pars | 530 | -0.3301 | -0.3450 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
