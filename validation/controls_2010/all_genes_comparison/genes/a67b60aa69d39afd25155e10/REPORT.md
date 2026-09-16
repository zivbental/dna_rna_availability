# YFR050C
Status: ok. Length: 959 nt. Measured usable bases: 685. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 685 | 0.3520 | 0.3392 |
| rnafold | ok | 685 | 0.2426 | 0.2451 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 523 | -0.2052 | -0.2506 |
| seed_p | 523 | -0.3586 | -0.2427 |
| seed_p_vs_seed_pars | 448 | -0.5639 | -0.3511 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
