# YOR299W
Status: ok. Length: 2241 nt. Measured usable bases: 1143. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1143 | 0.3504 | 0.3307 |
| rnafold | ok | 1143 | 0.2702 | 0.2612 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 242 | -0.1538 | -0.1689 |
| seed_p | 242 | -0.2406 | -0.2341 |
| seed_p_vs_seed_pars | 139 | -0.1789 | -0.2033 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
