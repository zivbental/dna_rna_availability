# YGL016W
Status: ok. Length: 3246 nt. Measured usable bases: 1430. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1430 | 0.3363 | 0.3180 |
| rnafold | ok | 1430 | 0.2249 | 0.2237 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 149 | -0.2150 | -0.4494 |
| seed_p | 149 | -0.2313 | -0.3343 |
| seed_p_vs_seed_pars | 90 | -0.1837 | -0.4460 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
