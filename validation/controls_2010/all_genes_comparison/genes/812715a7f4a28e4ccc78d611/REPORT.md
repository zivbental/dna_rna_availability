# YKL148C
Status: ok. Length: 2281 nt. Measured usable bases: 1114. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1114 | 0.3814 | 0.3799 |
| rnafold | ok | 1114 | 0.3213 | 0.3156 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 212 | -0.2529 | -0.2832 |
| seed_p | 212 | -0.1615 | -0.2258 |
| seed_p_vs_seed_pars | 159 | -0.3969 | -0.4507 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
