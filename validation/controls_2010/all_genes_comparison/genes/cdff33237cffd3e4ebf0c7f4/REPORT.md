# YKL034W
Status: ok. Length: 2394 nt. Measured usable bases: 1042. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1042 | 0.1979 | 0.1761 |
| rnafold | ok | 1042 | 0.1637 | 0.1541 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | 0.7321 | 0.7232 |
| seed_p | 87 | 0.4283 | 0.5174 |
| seed_p_vs_seed_pars | 48 | 0.0994 | -0.0557 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
