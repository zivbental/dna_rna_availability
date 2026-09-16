# YIL085C
Status: ok. Length: 1668 nt. Measured usable bases: 356. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 356 | 0.3471 | 0.3284 |
| rnafold | ok | 356 | 0.3009 | 0.2837 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 168 | -0.3326 | -0.0627 |
| seed_p | 168 | -0.0283 | -0.0669 |
| seed_p_vs_seed_pars | 146 | -0.2139 | 0.0243 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
