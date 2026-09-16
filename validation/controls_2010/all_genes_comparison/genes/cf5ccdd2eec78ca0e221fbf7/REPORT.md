# YGL077C
Status: ok. Length: 1811 nt. Measured usable bases: 1190. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1190 | 0.2098 | 0.1864 |
| rnafold | ok | 1190 | 0.2161 | 0.2174 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 546 | 0.0761 | -0.1136 |
| seed_p | 546 | -0.0773 | -0.1479 |
| seed_p_vs_seed_pars | 434 | -0.0388 | -0.1709 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
