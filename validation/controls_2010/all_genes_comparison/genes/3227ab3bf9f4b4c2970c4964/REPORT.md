# YKL212W
Status: ok. Length: 2304 nt. Measured usable bases: 1622. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1622 | 0.2858 | 0.2599 |
| rnafold | ok | 1622 | 0.2242 | 0.2001 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1166 | -0.0187 | 0.0688 |
| seed_p | 1166 | -0.0648 | -0.0054 |
| seed_p_vs_seed_pars | 926 | -0.1635 | -0.1321 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
