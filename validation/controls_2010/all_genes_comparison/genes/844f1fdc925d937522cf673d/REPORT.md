# YKL043W
Status: ok. Length: 1259 nt. Measured usable bases: 692. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 692 | 0.2785 | 0.2587 |
| rnafold | ok | 692 | 0.2153 | 0.2174 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 147 | 0.0408 | -0.1366 |
| seed_p | 147 | 0.1417 | 0.0947 |
| seed_p_vs_seed_pars | 109 | 0.1805 | 0.1359 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
