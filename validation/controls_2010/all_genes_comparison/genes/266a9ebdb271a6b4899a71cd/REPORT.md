# YGR124W
Status: ok. Length: 1849 nt. Measured usable bases: 1573. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1573 | 0.3107 | 0.3058 |
| rnafold | ok | 1573 | 0.2575 | 0.2541 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1440 | -0.1155 | -0.0948 |
| seed_p | 1440 | -0.2612 | -0.2434 |
| seed_p_vs_seed_pars | 1303 | -0.3648 | -0.3273 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
