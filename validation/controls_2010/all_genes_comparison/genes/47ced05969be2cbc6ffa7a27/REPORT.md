# YNL062C
Status: ok. Length: 1437 nt. Measured usable bases: 804. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 804 | 0.3301 | 0.3228 |
| rnafold | ok | 804 | 0.2903 | 0.2919 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 206 | -0.2090 | -0.2804 |
| seed_p | 206 | -0.0699 | -0.0695 |
| seed_p_vs_seed_pars | 167 | -0.1541 | -0.3601 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
