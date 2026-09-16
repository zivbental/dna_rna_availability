# YPL067C
Status: ok. Length: 729 nt. Measured usable bases: 379. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 379 | 0.3242 | 0.3161 |
| rnafold | ok | 379 | 0.2487 | 0.2377 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 103 | -0.2090 | -0.2969 |
| seed_p | 103 | 0.0170 | -0.0645 |
| seed_p_vs_seed_pars | 52 | -0.0722 | -0.2538 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
