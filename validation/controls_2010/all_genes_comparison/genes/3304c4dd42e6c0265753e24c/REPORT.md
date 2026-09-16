# YCR028C
Status: ok. Length: 1768 nt. Measured usable bases: 909. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 909 | 0.2951 | 0.2572 |
| rnafold | ok | 909 | 0.2251 | 0.2113 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 173 | -0.0863 | -0.1682 |
| seed_p | 173 | -0.3667 | -0.1769 |
| seed_p_vs_seed_pars | 144 | -0.2817 | 0.0304 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
