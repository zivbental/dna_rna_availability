# YBR030W
Status: ok. Length: 1838 nt. Measured usable bases: 624. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 624 | 0.3777 | 0.3646 |
| rnafold | ok | 624 | 0.3003 | 0.2938 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | -0.1019 | -0.1540 |
| seed_p | 71 | -0.6846 | -0.5922 |
| seed_p_vs_seed_pars | 59 | -0.5894 | -0.5342 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
