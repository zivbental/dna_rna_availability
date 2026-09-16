# YCR023C
Status: ok. Length: 2157 nt. Measured usable bases: 1177. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1177 | 0.2774 | 0.2502 |
| rnafold | ok | 1177 | 0.1879 | 0.1788 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 386 | -0.1116 | -0.1855 |
| seed_p | 386 | -0.3220 | -0.2454 |
| seed_p_vs_seed_pars | 309 | -0.3377 | -0.3129 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
