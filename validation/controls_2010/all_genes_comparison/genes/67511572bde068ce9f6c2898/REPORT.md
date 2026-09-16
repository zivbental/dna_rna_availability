# YER155C
Status: ok. Length: 6694 nt. Measured usable bases: 2792. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2792 | 0.2687 | 0.2529 |
| rnafold | ok | 2792 | 0.1922 | 0.1822 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 309 | 0.0360 | 0.0558 |
| seed_p | 309 | -0.0354 | 0.0157 |
| seed_p_vs_seed_pars | 216 | -0.1061 | -0.0892 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
