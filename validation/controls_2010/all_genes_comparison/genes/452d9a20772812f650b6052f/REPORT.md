# YOL021C
Status: ok. Length: 3125 nt. Measured usable bases: 1580. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1580 | 0.3373 | 0.3256 |
| rnafold | ok | 1580 | 0.2180 | 0.2192 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 210 | 0.0203 | 0.1426 |
| seed_p | 210 | -0.0114 | 0.0691 |
| seed_p_vs_seed_pars | 145 | -0.1485 | -0.2251 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
