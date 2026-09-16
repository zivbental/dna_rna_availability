# YLL051C
Status: ok. Length: 2373 nt. Measured usable bases: 1225. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1225 | 0.3160 | 0.2963 |
| rnafold | ok | 1225 | 0.2689 | 0.2524 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 240 | 0.0650 | -0.0437 |
| seed_p | 240 | -0.2252 | -0.1868 |
| seed_p_vs_seed_pars | 176 | 0.0184 | -0.0421 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
