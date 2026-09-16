# YMR272C
Status: ok. Length: 1340 nt. Measured usable bases: 968. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 968 | 0.2815 | 0.2606 |
| rnafold | ok | 968 | 0.2431 | 0.2578 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 552 | 0.1282 | 0.0317 |
| seed_p | 552 | 0.0099 | -0.0217 |
| seed_p_vs_seed_pars | 430 | -0.1290 | -0.1428 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
