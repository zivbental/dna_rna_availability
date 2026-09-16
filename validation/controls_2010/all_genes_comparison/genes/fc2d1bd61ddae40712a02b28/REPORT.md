# YMR258C
Status: ok. Length: 1722 nt. Measured usable bases: 768. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 768 | 0.3245 | 0.3060 |
| rnafold | ok | 768 | 0.2769 | 0.2569 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 73 | -0.1806 | -0.3011 |
| seed_p | 73 | -0.1959 | -0.2661 |
| seed_p_vs_seed_pars | 42 | -0.4065 | -0.5981 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
