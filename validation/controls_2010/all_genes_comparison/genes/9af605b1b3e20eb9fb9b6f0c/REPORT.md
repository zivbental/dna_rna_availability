# YNL241C
Status: ok. Length: 1772 nt. Measured usable bases: 1278. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1278 | 0.3920 | 0.3753 |
| rnafold | ok | 1278 | 0.3344 | 0.3263 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 922 | -0.0721 | -0.1075 |
| seed_p | 922 | -0.1515 | -0.0318 |
| seed_p_vs_seed_pars | 704 | -0.1521 | -0.1326 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
