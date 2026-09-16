# YOR133W
Status: ok. Length: 2777 nt. Measured usable bases: 243. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 243 | 0.3320 | 0.2831 |
| rnafold | ok | 243 | 0.3543 | 0.3239 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 116 | -0.1618 | -0.0656 |
| seed_p | 116 | -0.3653 | -0.2800 |
| seed_p_vs_seed_pars | 111 | -0.2957 | -0.2875 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
