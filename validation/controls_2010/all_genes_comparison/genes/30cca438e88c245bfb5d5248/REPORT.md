# YLR241W
Status: ok. Length: 2349 nt. Measured usable bases: 1212. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1212 | 0.2733 | 0.2679 |
| rnafold | ok | 1212 | 0.2290 | 0.2157 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 308 | -0.1403 | -0.2996 |
| seed_p | 308 | -0.2071 | -0.1789 |
| seed_p_vs_seed_pars | 219 | -0.2572 | -0.2752 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
