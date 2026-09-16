# YMR015C
Status: ok. Length: 1935 nt. Measured usable bases: 1261. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1261 | 0.2739 | 0.2506 |
| rnafold | ok | 1261 | 0.1273 | 0.1175 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 678 | -0.0810 | 0.0673 |
| seed_p | 678 | -0.1716 | -0.0750 |
| seed_p_vs_seed_pars | 511 | -0.2146 | -0.1931 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
