# YGR281W
Status: ok. Length: 4816 nt. Measured usable bases: 1859. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1859 | 0.2709 | 0.2564 |
| rnafold | ok | 1859 | 0.2212 | 0.2130 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 149 | 0.2669 | 0.4778 |
| seed_p | 149 | 0.2062 | 0.3497 |
| seed_p_vs_seed_pars | 113 | 0.0363 | 0.1358 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
