# YIL153W
Status: ok. Length: 1242 nt. Measured usable bases: 715. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 715 | 0.2594 | 0.2511 |
| rnafold | ok | 715 | 0.2265 | 0.2159 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 256 | -0.1518 | 0.0956 |
| seed_p | 256 | 0.0741 | 0.1600 |
| seed_p_vs_seed_pars | 214 | 0.0672 | 0.0834 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
