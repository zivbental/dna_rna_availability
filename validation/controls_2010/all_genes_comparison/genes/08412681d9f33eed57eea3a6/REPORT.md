# YOR157C
Status: ok. Length: 857 nt. Measured usable bases: 597. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 597 | 0.3222 | 0.2879 |
| rnafold | ok | 597 | 0.2545 | 0.2237 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 370 | -0.0536 | -0.2250 |
| seed_p | 370 | 0.0962 | 0.0936 |
| seed_p_vs_seed_pars | 300 | -0.0313 | -0.0823 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
