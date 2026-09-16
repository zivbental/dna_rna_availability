# YLR314C
Status: ok. Length: 1716 nt. Measured usable bases: 835. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 835 | 0.2829 | 0.2631 |
| rnafold | ok | 835 | 0.2513 | 0.2381 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 173 | -0.2076 | -0.1351 |
| seed_p | 173 | -0.0528 | 0.0367 |
| seed_p_vs_seed_pars | 95 | -0.5537 | -0.5031 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
