# YMR073C
Status: ok. Length: 1401 nt. Measured usable bases: 349. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 349 | 0.3221 | 0.3007 |
| rnafold | ok | 349 | 0.2684 | 0.2345 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 84 | -0.6186 | -0.8650 |
| seed_p | 84 | -0.5843 | -0.6291 |
| seed_p_vs_seed_pars | 52 | -0.6841 | -0.7483 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
