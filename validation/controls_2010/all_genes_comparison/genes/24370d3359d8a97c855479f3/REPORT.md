# YGL135W
Status: ok. Length: 813 nt. Measured usable bases: 151. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 151 | 0.2042 | 0.1542 |
| rnafold | ok | 151 | 0.2507 | 0.2447 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 92 | -0.0429 | 0.2227 |
| seed_p | 92 | 0.0775 | 0.0991 |
| seed_p_vs_seed_pars | 88 | 0.2427 | 0.1031 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
