# YMR209C
Status: ok. Length: 2455 nt. Measured usable bases: 714. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 714 | 0.3268 | 0.3263 |
| rnafold | ok | 714 | 0.2748 | 0.2823 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 140 | -0.2188 | -0.0018 |
| seed_p | 140 | -0.0073 | 0.1786 |
| seed_p_vs_seed_pars | 116 | -0.0131 | 0.1894 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
