# YER064C
Status: ok. Length: 1843 nt. Measured usable bases: 952. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 952 | 0.2720 | 0.2769 |
| rnafold | ok | 952 | 0.2111 | 0.2113 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 176 | 0.0103 | 0.1456 |
| seed_p | 176 | -0.2031 | -0.1687 |
| seed_p_vs_seed_pars | 131 | -0.5262 | -0.4905 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
