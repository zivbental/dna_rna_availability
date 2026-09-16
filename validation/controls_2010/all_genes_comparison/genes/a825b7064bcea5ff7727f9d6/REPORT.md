# YLL018C-A
Status: ok. Length: 415 nt. Measured usable bases: 257. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 257 | 0.2803 | 0.2634 |
| rnafold | ok | 257 | 0.2868 | 0.2696 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 117 | -0.5162 | -0.6587 |
| seed_p | 117 | -0.6122 | -0.4711 |
| seed_p_vs_seed_pars | 103 | -0.5968 | -0.4442 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
