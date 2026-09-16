# YLL045C
Status: ok. Length: 849 nt. Measured usable bases: 371. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 371 | 0.2352 | 0.2307 |
| rnafold | ok | 371 | 0.2444 | 0.2521 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 133 | -0.2734 | 0.0269 |
| seed_p | 133 | -0.4693 | -0.4112 |
| seed_p_vs_seed_pars | 88 | -0.3459 | -0.4261 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
