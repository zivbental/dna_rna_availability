# YGL255W
Status: ok. Length: 1265 nt. Measured usable bases: 665. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 665 | 0.3100 | 0.3025 |
| rnafold | ok | 665 | 0.2163 | 0.2422 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 158 | 0.0619 | 0.3299 |
| seed_p | 158 | 0.0789 | 0.1516 |
| seed_p_vs_seed_pars | 122 | -0.1340 | 0.0678 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
