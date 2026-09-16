# YPL010W
Status: ok. Length: 785 nt. Measured usable bases: 651. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 651 | 0.2495 | 0.2181 |
| rnafold | ok | 651 | 0.2634 | 0.2621 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 576 | 0.1570 | 0.2910 |
| seed_p | 576 | -0.0366 | -0.0283 |
| seed_p_vs_seed_pars | 525 | 0.0042 | 0.0397 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
