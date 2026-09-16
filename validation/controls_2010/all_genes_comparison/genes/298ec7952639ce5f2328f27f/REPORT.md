# YGL080W
Status: ok. Length: 711 nt. Measured usable bases: 322. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 322 | 0.2523 | 0.2423 |
| rnafold | ok | 322 | 0.2379 | 0.2221 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 74 | 0.1256 | 0.1309 |
| seed_p | 74 | -0.0986 | -0.0533 |
| seed_p_vs_seed_pars | 52 | -0.2272 | -0.0741 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
