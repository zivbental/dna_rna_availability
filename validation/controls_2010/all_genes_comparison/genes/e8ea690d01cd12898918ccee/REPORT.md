# YGL166W
Status: ok. Length: 861 nt. Measured usable bases: 455. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 455 | 0.3187 | 0.3278 |
| rnafold | ok | 455 | 0.2934 | 0.2966 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 151 | -0.1126 | 0.1351 |
| seed_p | 151 | -0.0351 | -0.0382 |
| seed_p_vs_seed_pars | 105 | 0.2903 | 0.0266 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
