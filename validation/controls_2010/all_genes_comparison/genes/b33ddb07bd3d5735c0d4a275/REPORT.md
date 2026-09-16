# YLR085C
Status: ok. Length: 1412 nt. Measured usable bases: 506. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 506 | 0.3225 | 0.3264 |
| rnafold | ok | 506 | 0.3398 | 0.3408 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | 0.5319 | 0.5199 |
| seed_p | 31 | 0.7031 | 0.8388 |
| seed_p_vs_seed_pars | 22 | 0.5408 | 0.7319 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
