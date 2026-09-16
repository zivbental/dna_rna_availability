# YMR130W
Status: ok. Length: 1064 nt. Measured usable bases: 631. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 631 | 0.3029 | 0.2893 |
| rnafold | ok | 631 | 0.2768 | 0.2618 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 275 | -0.1544 | -0.0141 |
| seed_p | 275 | -0.2760 | -0.2128 |
| seed_p_vs_seed_pars | 174 | 0.0292 | 0.1205 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
