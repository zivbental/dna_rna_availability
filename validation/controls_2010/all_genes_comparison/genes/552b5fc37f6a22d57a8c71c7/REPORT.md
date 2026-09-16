# YMR184W
Status: ok. Length: 702 nt. Measured usable bases: 418. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 418 | 0.2873 | 0.2813 |
| rnafold | ok | 418 | 0.2276 | 0.2786 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 226 | 0.0378 | -0.0261 |
| seed_p | 226 | -0.1176 | -0.1541 |
| seed_p_vs_seed_pars | 167 | -0.4600 | -0.3556 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
