# YBR122C
Status: ok. Length: 740 nt. Measured usable bases: 422. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 422 | 0.3360 | 0.3296 |
| rnafold | ok | 422 | 0.1821 | 0.1850 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 145 | 0.0489 | 0.2091 |
| seed_p | 145 | 0.2535 | 0.2698 |
| seed_p_vs_seed_pars | 77 | 0.3641 | 0.4497 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
