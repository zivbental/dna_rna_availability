# YMR123W
Status: ok. Length: 443 nt. Measured usable bases: 329. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 329 | 0.1944 | 0.2003 |
| rnafold | ok | 329 | 0.1430 | 0.1575 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 238 | 0.2068 | 0.2007 |
| seed_p | 238 | 0.2226 | 0.2927 |
| seed_p_vs_seed_pars | 198 | 0.0891 | 0.0665 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
