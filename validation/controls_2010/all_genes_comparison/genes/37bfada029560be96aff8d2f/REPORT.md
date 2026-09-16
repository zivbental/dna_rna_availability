# YDR232W
Status: ok. Length: 2052 nt. Measured usable bases: 1496. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1496 | 0.3204 | 0.3064 |
| rnafold | ok | 1496 | 0.2328 | 0.2260 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1256 | 0.0155 | -0.2187 |
| seed_p | 1256 | -0.1431 | -0.1583 |
| seed_p_vs_seed_pars | 1040 | -0.2434 | -0.2618 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
