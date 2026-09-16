# YGR119C
Status: ok. Length: 1750 nt. Measured usable bases: 897. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 897 | 0.3359 | 0.3208 |
| rnafold | ok | 897 | 0.2390 | 0.2483 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 195 | 0.0910 | -0.0792 |
| seed_p | 195 | 0.0145 | 0.0290 |
| seed_p_vs_seed_pars | 161 | -0.2282 | -0.2598 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
