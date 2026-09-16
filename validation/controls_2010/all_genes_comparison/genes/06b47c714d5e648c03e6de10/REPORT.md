# YBR112C
Status: ok. Length: 3188 nt. Measured usable bases: 1337. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1337 | 0.1906 | 0.1757 |
| rnafold | ok | 1337 | 0.2143 | 0.2060 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 140 | -0.2719 | -0.2634 |
| seed_p | 140 | -0.3724 | -0.3780 |
| seed_p_vs_seed_pars | 108 | -0.5750 | -0.4749 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
