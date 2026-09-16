# YML016C
Status: ok. Length: 2471 nt. Measured usable bases: 990. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 990 | 0.2689 | 0.2547 |
| rnafold | ok | 990 | 0.2001 | 0.1805 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 127 | -0.0744 | -0.0751 |
| seed_p | 127 | -0.4900 | -0.4154 |
| seed_p_vs_seed_pars | 86 | -0.5775 | -0.5794 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
