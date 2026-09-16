# YKL210W
Status: ok. Length: 3212 nt. Measured usable bases: 2401. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2401 | 0.3126 | 0.2890 |
| rnafold | ok | 2401 | 0.3027 | 0.2783 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1856 | -0.0064 | -0.0782 |
| seed_p | 1856 | -0.1442 | -0.1309 |
| seed_p_vs_seed_pars | 1466 | -0.2460 | -0.1886 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
