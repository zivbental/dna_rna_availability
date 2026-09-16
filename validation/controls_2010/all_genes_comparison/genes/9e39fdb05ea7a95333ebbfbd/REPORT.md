# YDR167W
Status: ok. Length: 725 nt. Measured usable bases: 373. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 373 | 0.3177 | 0.3207 |
| rnafold | ok | 373 | 0.3579 | 0.3616 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 109 | 0.1020 | 0.2689 |
| seed_p | 109 | 0.1712 | 0.1800 |
| seed_p_vs_seed_pars | 91 | 0.2551 | 0.2025 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
