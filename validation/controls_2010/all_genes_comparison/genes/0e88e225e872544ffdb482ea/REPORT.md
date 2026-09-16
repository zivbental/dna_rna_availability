# YNR015W
Status: ok. Length: 1203 nt. Measured usable bases: 792. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 792 | 0.3146 | 0.3035 |
| rnafold | ok | 792 | 0.2273 | 0.2251 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 332 | -0.1694 | -0.0088 |
| seed_p | 332 | -0.1302 | -0.0755 |
| seed_p_vs_seed_pars | 293 | -0.0169 | -0.0461 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
