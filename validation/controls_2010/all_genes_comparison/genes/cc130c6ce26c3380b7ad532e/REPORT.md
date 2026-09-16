# YGL021W
Status: ok. Length: 2387 nt. Measured usable bases: 1035. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1035 | 0.2839 | 0.2389 |
| rnafold | ok | 1035 | 0.2729 | 0.2425 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | -0.1511 | -0.0738 |
| seed_p | 143 | -0.0119 | -0.0218 |
| seed_p_vs_seed_pars | 111 | -0.4026 | -0.3193 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
