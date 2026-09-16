# YHR001W
Status: ok. Length: 1704 nt. Measured usable bases: 695. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 695 | 0.4350 | 0.4112 |
| rnafold | ok | 695 | 0.3938 | 0.3666 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | -0.1456 | 0.0500 |
| seed_p | 87 | -0.2666 | -0.1547 |
| seed_p_vs_seed_pars | 69 | -0.5264 | -0.3080 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
