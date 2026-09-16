# YPL039W
Status: ok. Length: 1117 nt. Measured usable bases: 373. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 373 | 0.2162 | 0.2216 |
| rnafold | ok | 373 | 0.2324 | 0.2227 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 39 | -0.5791 | -0.5903 |
| seed_p | 39 | -0.7386 | -0.6818 |
| seed_p_vs_seed_pars | 30 | -0.3334 | -0.6587 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
