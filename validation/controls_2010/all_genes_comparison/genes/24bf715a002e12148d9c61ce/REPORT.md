# YGL257C
Status: ok. Length: 1853 nt. Measured usable bases: 898. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 898 | 0.2603 | 0.2514 |
| rnafold | ok | 898 | 0.2329 | 0.2321 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 138 | 0.0323 | -0.0684 |
| seed_p | 138 | -0.1035 | -0.0671 |
| seed_p_vs_seed_pars | 114 | -0.1885 | -0.1301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
