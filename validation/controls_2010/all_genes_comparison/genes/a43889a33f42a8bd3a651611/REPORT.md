# YPL048W
Status: ok. Length: 1463 nt. Measured usable bases: 1137. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1137 | 0.3172 | 0.3058 |
| rnafold | ok | 1137 | 0.2684 | 0.2670 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 949 | -0.0704 | -0.0992 |
| seed_p | 949 | -0.1946 | -0.2204 |
| seed_p_vs_seed_pars | 787 | -0.3422 | -0.4164 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
