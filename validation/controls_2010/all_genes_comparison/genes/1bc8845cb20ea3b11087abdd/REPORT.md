# YGL120C
Status: ok. Length: 2442 nt. Measured usable bases: 1606. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1606 | 0.2754 | 0.2656 |
| rnafold | ok | 1606 | 0.2122 | 0.2211 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 899 | -0.2473 | -0.3430 |
| seed_p | 899 | -0.2534 | -0.3049 |
| seed_p_vs_seed_pars | 665 | -0.2660 | -0.3441 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
