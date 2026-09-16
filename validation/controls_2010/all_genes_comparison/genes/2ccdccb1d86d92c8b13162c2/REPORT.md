# YHL007C
Status: ok. Length: 2939 nt. Measured usable bases: 1184. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1184 | 0.3016 | 0.2856 |
| rnafold | ok | 1184 | 0.3192 | 0.3020 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 74 | -0.1271 | -0.1394 |
| seed_p | 74 | -0.2298 | -0.1259 |
| seed_p_vs_seed_pars | 57 | -0.4367 | -0.5221 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
