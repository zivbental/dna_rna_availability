# YPL207W
Status: ok. Length: 2606 nt. Measured usable bases: 1255. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1255 | 0.3720 | 0.3519 |
| rnafold | ok | 1255 | 0.2951 | 0.2986 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 283 | -0.2588 | -0.3961 |
| seed_p | 283 | -0.2896 | -0.2655 |
| seed_p_vs_seed_pars | 207 | -0.5352 | -0.4615 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
