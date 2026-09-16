# YDR226W
Status: ok. Length: 842 nt. Measured usable bases: 751. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 751 | 0.3368 | 0.3468 |
| rnafold | ok | 751 | 0.2693 | 0.3071 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 708 | -0.2655 | -0.2221 |
| seed_p | 708 | -0.2925 | -0.2320 |
| seed_p_vs_seed_pars | 670 | -0.3384 | -0.1842 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
