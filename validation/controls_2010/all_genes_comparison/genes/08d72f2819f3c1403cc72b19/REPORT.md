# YDL060W
Status: ok. Length: 2507 nt. Measured usable bases: 1143. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1143 | 0.3706 | 0.3551 |
| rnafold | ok | 1143 | 0.3592 | 0.3581 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 158 | -0.2146 | -0.2309 |
| seed_p | 158 | -0.0658 | -0.1543 |
| seed_p_vs_seed_pars | 121 | -0.3796 | -0.2592 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
