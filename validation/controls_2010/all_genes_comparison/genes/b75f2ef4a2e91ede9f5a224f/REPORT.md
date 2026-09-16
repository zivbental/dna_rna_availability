# YGL114W
Status: ok. Length: 2298 nt. Measured usable bases: 1073. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1073 | 0.3324 | 0.3368 |
| rnafold | ok | 1073 | 0.3008 | 0.2931 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 112 | -0.1116 | -0.2512 |
| seed_p | 112 | -0.6716 | -0.6545 |
| seed_p_vs_seed_pars | 85 | -0.7985 | -0.7362 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
