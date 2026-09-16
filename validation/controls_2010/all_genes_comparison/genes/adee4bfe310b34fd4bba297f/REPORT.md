# YER036C
Status: ok. Length: 1940 nt. Measured usable bases: 1611. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1611 | 0.3373 | 0.3274 |
| rnafold | ok | 1611 | 0.2219 | 0.2233 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1393 | -0.1084 | -0.0256 |
| seed_p | 1393 | -0.1952 | -0.1247 |
| seed_p_vs_seed_pars | 1147 | -0.3289 | -0.1806 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
