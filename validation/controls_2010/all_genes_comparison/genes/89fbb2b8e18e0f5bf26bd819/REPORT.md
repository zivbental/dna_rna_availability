# YIL030C
Status: ok. Length: 4038 nt. Measured usable bases: 2285. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2285 | 0.2775 | 0.2524 |
| rnafold | ok | 2285 | 0.2463 | 0.2192 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 684 | 0.0525 | -0.0308 |
| seed_p | 684 | -0.0858 | -0.0733 |
| seed_p_vs_seed_pars | 545 | -0.1487 | -0.1783 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
