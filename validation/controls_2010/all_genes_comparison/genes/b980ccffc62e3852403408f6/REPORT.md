# YBR143C
Status: ok. Length: 1452 nt. Measured usable bases: 1069. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1069 | 0.2773 | 0.2676 |
| rnafold | ok | 1069 | 0.1817 | 0.1784 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 830 | 0.1431 | -0.0145 |
| seed_p | 830 | -0.2321 | -0.1234 |
| seed_p_vs_seed_pars | 695 | -0.3096 | -0.2624 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
