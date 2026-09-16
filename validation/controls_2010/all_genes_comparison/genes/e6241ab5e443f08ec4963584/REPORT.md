# YPL019C
Status: ok. Length: 2689 nt. Measured usable bases: 2202. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2202 | 0.3465 | 0.3318 |
| rnafold | ok | 2202 | 0.2923 | 0.2836 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1892 | -0.0981 | -0.2558 |
| seed_p | 1892 | -0.2060 | -0.2440 |
| seed_p_vs_seed_pars | 1628 | -0.3514 | -0.3205 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
