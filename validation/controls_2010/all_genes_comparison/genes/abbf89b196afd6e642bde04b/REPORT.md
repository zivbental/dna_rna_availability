# YGR074W
Status: ok. Length: 736 nt. Measured usable bases: 410. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 410 | 0.3258 | 0.3322 |
| rnafold | ok | 410 | 0.2201 | 0.2292 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | 0.4304 | 0.0831 |
| seed_p | 135 | 0.3844 | 0.2722 |
| seed_p_vs_seed_pars | 89 | 0.4260 | 0.3895 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
