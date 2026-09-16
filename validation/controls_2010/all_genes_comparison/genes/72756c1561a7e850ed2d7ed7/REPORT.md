# YNL219C
Status: ok. Length: 2977 nt. Measured usable bases: 1189. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1189 | 0.3300 | 0.3203 |
| rnafold | ok | 1189 | 0.2466 | 0.2317 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 513 | -0.2184 | -0.2368 |
| seed_p | 513 | -0.3517 | -0.2912 |
| seed_p_vs_seed_pars | 341 | -0.5993 | -0.5064 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
