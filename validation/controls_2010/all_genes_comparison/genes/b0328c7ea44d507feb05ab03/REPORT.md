# YML129C
Status: ok. Length: 393 nt. Measured usable bases: 198. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 198 | 0.1394 | 0.1333 |
| rnafold | ok | 198 | 0.0870 | 0.1157 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 42 | 0.2023 | 0.1694 |
| seed_p | 42 | -0.4950 | -0.6132 |
| seed_p_vs_seed_pars | 40 | -0.6015 | -0.6795 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
