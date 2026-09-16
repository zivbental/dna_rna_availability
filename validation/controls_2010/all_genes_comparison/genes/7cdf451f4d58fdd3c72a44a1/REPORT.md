# YHR206W
Status: ok. Length: 2467 nt. Measured usable bases: 1131. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1131 | 0.3057 | 0.2988 |
| rnafold | ok | 1131 | 0.2403 | 0.2348 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 173 | -0.0849 | -0.2336 |
| seed_p | 173 | -0.2986 | -0.3073 |
| seed_p_vs_seed_pars | 115 | -0.6838 | -0.6969 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
