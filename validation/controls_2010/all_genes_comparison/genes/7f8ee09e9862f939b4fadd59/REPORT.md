# YLR007W
Status: ok. Length: 1077 nt. Measured usable bases: 564. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 564 | -0.0078 | 0.0177 |
| rnafold | ok | 564 | -0.0015 | 0.0291 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | -0.2077 | -0.3429 |
| seed_p | 118 | -0.4382 | -0.4776 |
| seed_p_vs_seed_pars | 97 | -0.5753 | -0.5458 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
