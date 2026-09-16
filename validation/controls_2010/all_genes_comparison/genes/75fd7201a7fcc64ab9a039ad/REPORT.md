# YER174C
Status: ok. Length: 820 nt. Measured usable bases: 524. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 524 | 0.3350 | 0.3270 |
| rnafold | ok | 524 | 0.3171 | 0.3106 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 300 | -0.1704 | -0.1669 |
| seed_p | 300 | 0.0269 | 0.0956 |
| seed_p_vs_seed_pars | 246 | -0.1468 | -0.1268 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
