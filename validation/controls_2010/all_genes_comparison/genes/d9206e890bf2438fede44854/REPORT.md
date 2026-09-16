# YDR284C
Status: ok. Length: 1200 nt. Measured usable bases: 851. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 851 | 0.2518 | 0.2508 |
| rnafold | ok | 851 | 0.1298 | 0.1241 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 540 | -0.1677 | -0.1940 |
| seed_p | 540 | -0.0580 | -0.0918 |
| seed_p_vs_seed_pars | 456 | -0.1995 | -0.2740 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
