# YLR003C
Status: ok. Length: 978 nt. Measured usable bases: 333. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 333 | 0.2833 | 0.2638 |
| rnafold | ok | 333 | 0.1740 | 0.1656 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 33 | 0.0167 | 0.1655 |
| seed_p | 33 | 0.2426 | 0.2660 |
| seed_p_vs_seed_pars | 20 | 0.1033 | 0.5600 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
