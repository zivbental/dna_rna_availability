# YER027C
Status: ok. Length: 1382 nt. Measured usable bases: 811. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 811 | 0.2230 | 0.2060 |
| rnafold | ok | 811 | 0.2219 | 0.2105 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 249 | -0.2316 | -0.0924 |
| seed_p | 249 | -0.2833 | -0.2025 |
| seed_p_vs_seed_pars | 211 | -0.2334 | -0.2312 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
