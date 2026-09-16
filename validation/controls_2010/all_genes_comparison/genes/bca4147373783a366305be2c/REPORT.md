# YDR529C
Status: ok. Length: 600 nt. Measured usable bases: 362. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 362 | 0.3161 | 0.3153 |
| rnafold | ok | 362 | 0.3686 | 0.3588 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 159 | 0.2008 | 0.1356 |
| seed_p | 159 | -0.1061 | -0.1990 |
| seed_p_vs_seed_pars | 105 | 0.3437 | 0.2474 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
