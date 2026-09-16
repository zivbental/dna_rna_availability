# YHR073W
Status: ok. Length: 3217 nt. Measured usable bases: 1329. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1329 | 0.3027 | 0.2915 |
| rnafold | ok | 1329 | 0.2934 | 0.2886 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 205 | 0.0789 | 0.1244 |
| seed_p | 205 | 0.0586 | 0.0763 |
| seed_p_vs_seed_pars | 152 | -0.1392 | -0.3012 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
