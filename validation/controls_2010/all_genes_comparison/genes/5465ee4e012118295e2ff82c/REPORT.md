# YOR243C
Status: ok. Length: 2193 nt. Measured usable bases: 1141. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1141 | 0.3269 | 0.3196 |
| rnafold | ok | 1141 | 0.2593 | 0.2557 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 204 | -0.2456 | -0.2151 |
| seed_p | 204 | -0.4740 | -0.4206 |
| seed_p_vs_seed_pars | 125 | -0.6558 | -0.5456 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
