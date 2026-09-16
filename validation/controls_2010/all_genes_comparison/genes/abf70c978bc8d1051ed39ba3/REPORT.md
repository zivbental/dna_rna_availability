# YDR054C
Status: ok. Length: 1400 nt. Measured usable bases: 596. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 596 | 0.2928 | 0.2986 |
| rnafold | ok | 596 | 0.2040 | 0.1883 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 38 | 0.2126 | 0.2863 |
| seed_p | 38 | -0.2774 | -0.4689 |
| seed_p_vs_seed_pars | 22 | -0.6687 | -0.7167 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
