# YDR233C
Status: ok. Length: 991 nt. Measured usable bases: 811. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 811 | 0.3273 | 0.3139 |
| rnafold | ok | 811 | 0.2679 | 0.2522 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 766 | -0.1497 | -0.0671 |
| seed_p | 766 | -0.1988 | -0.1039 |
| seed_p_vs_seed_pars | 708 | -0.2994 | -0.2366 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
