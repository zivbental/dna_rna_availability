# YPL170W
Status: ok. Length: 763 nt. Measured usable bases: 319. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 319 | 0.3828 | 0.3644 |
| rnafold | ok | 319 | 0.4157 | 0.4293 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 86 | 0.0946 | 0.1751 |
| seed_p | 86 | 0.2024 | 0.3048 |
| seed_p_vs_seed_pars | 71 | -0.6424 | -0.7603 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
