# YCR017C
Status: ok. Length: 3077 nt. Measured usable bases: 1834. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1834 | 0.2873 | 0.2666 |
| rnafold | ok | 1834 | 0.2273 | 0.2023 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 632 | -0.0277 | -0.0818 |
| seed_p | 632 | -0.1296 | -0.1508 |
| seed_p_vs_seed_pars | 449 | -0.4483 | -0.3644 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
