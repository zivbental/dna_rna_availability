# YGL157W
Status: ok. Length: 1172 nt. Measured usable bases: 671. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 671 | 0.3562 | 0.3459 |
| rnafold | ok | 671 | 0.3296 | 0.3079 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 195 | -0.2545 | -0.4296 |
| seed_p | 195 | -0.2795 | -0.2219 |
| seed_p_vs_seed_pars | 156 | -0.2429 | -0.2203 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
