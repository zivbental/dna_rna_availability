# YFL046W
Status: ok. Length: 803 nt. Measured usable bases: 282. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 282 | 0.2281 | 0.2330 |
| rnafold | ok | 282 | 0.2396 | 0.2396 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 40 | 0.4953 | 0.5832 |
| seed_p | 40 | 0.4636 | 0.2031 |
| seed_p_vs_seed_pars | 34 | 0.5104 | 0.2234 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
