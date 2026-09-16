# YOR210W
Status: ok. Length: 538 nt. Measured usable bases: 368. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 368 | 0.3131 | 0.3144 |
| rnafold | ok | 368 | 0.2487 | 0.2378 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 208 | -0.3815 | -0.4965 |
| seed_p | 208 | -0.3874 | -0.3696 |
| seed_p_vs_seed_pars | 148 | -0.2721 | -0.2679 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
