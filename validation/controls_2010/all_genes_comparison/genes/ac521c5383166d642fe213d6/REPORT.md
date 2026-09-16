# YNR050C
Status: ok. Length: 1535 nt. Measured usable bases: 1145. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1145 | 0.3135 | 0.2813 |
| rnafold | ok | 1145 | 0.2336 | 0.2079 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 825 | -0.1612 | -0.0099 |
| seed_p | 825 | -0.0992 | -0.1238 |
| seed_p_vs_seed_pars | 666 | -0.1632 | -0.2201 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
