# YIL115C
Status: ok. Length: 4577 nt. Measured usable bases: 1855. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1855 | 0.3299 | 0.3274 |
| rnafold | ok | 1855 | 0.2290 | 0.2381 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 178 | -0.1829 | -0.3416 |
| seed_p | 178 | -0.2067 | -0.1166 |
| seed_p_vs_seed_pars | 113 | 0.0877 | 0.2579 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
