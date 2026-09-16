# YHR046C
Status: ok. Length: 1104 nt. Measured usable bases: 406. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 406 | 0.4317 | 0.4030 |
| rnafold | ok | 406 | 0.3689 | 0.3733 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | 0.1823 | 0.2006 |
| seed_p | 34 | 0.3212 | 0.3284 |
| seed_p_vs_seed_pars | 22 | 0.5909 | 0.4345 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
