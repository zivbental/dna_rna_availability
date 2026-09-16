# YNR013C
Status: ok. Length: 2799 nt. Measured usable bases: 1652. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1652 | 0.2287 | 0.2114 |
| rnafold | ok | 1652 | 0.1848 | 0.1724 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 599 | -0.0063 | -0.0682 |
| seed_p | 599 | -0.0989 | -0.1326 |
| seed_p_vs_seed_pars | 464 | -0.1464 | -0.2200 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
