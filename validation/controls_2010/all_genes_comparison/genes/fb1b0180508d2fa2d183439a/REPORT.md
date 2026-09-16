# YHR143W-A
Status: ok. Length: 520 nt. Measured usable bases: 291. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 291 | 0.3447 | 0.3639 |
| rnafold | ok | 291 | 0.3211 | 0.3903 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 206 | -0.0350 | 0.1042 |
| seed_p | 206 | 0.0226 | 0.0378 |
| seed_p_vs_seed_pars | 189 | 0.1895 | 0.1472 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
