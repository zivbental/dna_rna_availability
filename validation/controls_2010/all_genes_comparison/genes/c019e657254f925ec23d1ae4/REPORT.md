# YFR037C
Status: ok. Length: 1792 nt. Measured usable bases: 1088. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1088 | 0.3962 | 0.3985 |
| rnafold | ok | 1088 | 0.3059 | 0.2921 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 466 | -0.0953 | -0.1195 |
| seed_p | 466 | -0.1093 | -0.1382 |
| seed_p_vs_seed_pars | 330 | -0.2006 | -0.2055 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
