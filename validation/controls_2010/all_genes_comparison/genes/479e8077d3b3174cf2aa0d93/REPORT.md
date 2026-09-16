# YDR395W
Status: ok. Length: 3034 nt. Measured usable bases: 1835. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1835 | 0.3194 | 0.3012 |
| rnafold | ok | 1835 | 0.2321 | 0.2318 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 702 | -0.0644 | 0.0265 |
| seed_p | 702 | -0.2384 | -0.1653 |
| seed_p_vs_seed_pars | 455 | -0.1321 | -0.0870 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
