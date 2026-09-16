# YDR047W
Status: ok. Length: 1362 nt. Measured usable bases: 836. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 836 | 0.4061 | 0.3814 |
| rnafold | ok | 836 | 0.3939 | 0.3687 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 377 | 0.0261 | -0.1609 |
| seed_p | 377 | -0.1309 | -0.0773 |
| seed_p_vs_seed_pars | 282 | -0.2838 | -0.0738 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
