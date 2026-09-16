# YHR068W
Status: ok. Length: 1378 nt. Measured usable bases: 1025. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1025 | 0.3040 | 0.2801 |
| rnafold | ok | 1025 | 0.2529 | 0.2472 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 857 | -0.0357 | 0.0050 |
| seed_p | 857 | -0.0762 | -0.1417 |
| seed_p_vs_seed_pars | 706 | -0.1872 | -0.2000 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
