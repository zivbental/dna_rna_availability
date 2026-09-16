# YER090W
Status: ok. Length: 1680 nt. Measured usable bases: 1166. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1166 | 0.2978 | 0.2835 |
| rnafold | ok | 1166 | 0.2716 | 0.2707 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 630 | 0.0226 | -0.1242 |
| seed_p | 630 | -0.1036 | -0.1652 |
| seed_p_vs_seed_pars | 475 | -0.3583 | -0.3567 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
