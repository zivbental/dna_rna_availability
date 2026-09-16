# YLR328W
Status: ok. Length: 1560 nt. Measured usable bases: 825. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 825 | 0.2828 | 0.2803 |
| rnafold | ok | 825 | 0.2158 | 0.2183 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 221 | -0.1462 | -0.1459 |
| seed_p | 221 | -0.0269 | 0.1527 |
| seed_p_vs_seed_pars | 146 | 0.0021 | 0.0438 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
