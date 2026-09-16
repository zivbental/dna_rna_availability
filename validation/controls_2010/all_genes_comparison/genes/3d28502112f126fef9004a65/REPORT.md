# YBR187W
Status: ok. Length: 1047 nt. Measured usable bases: 874. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 874 | 0.2837 | 0.2654 |
| rnafold | ok | 874 | 0.2356 | 0.2112 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 811 | 0.0578 | -0.1209 |
| seed_p | 811 | -0.0530 | -0.0020 |
| seed_p_vs_seed_pars | 737 | -0.2284 | -0.1962 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
