# YBR262C
Status: ok. Length: 420 nt. Measured usable bases: 233. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 233 | 0.4284 | 0.4159 |
| rnafold | ok | 233 | 0.2841 | 0.3112 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | -0.3149 | 0.0768 |
| seed_p | 61 | -0.2538 | -0.4103 |
| seed_p_vs_seed_pars | 46 | -0.0034 | -0.1427 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
