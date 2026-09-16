# YLR378C
Status: ok. Length: 1793 nt. Measured usable bases: 1427. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1427 | 0.3521 | 0.3376 |
| rnafold | ok | 1427 | 0.2536 | 0.2586 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1151 | -0.1974 | -0.1618 |
| seed_p | 1151 | -0.2074 | -0.1600 |
| seed_p_vs_seed_pars | 918 | -0.2603 | -0.2796 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
