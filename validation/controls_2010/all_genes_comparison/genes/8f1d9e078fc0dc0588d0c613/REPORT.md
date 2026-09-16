# YER050C
Status: ok. Length: 534 nt. Measured usable bases: 265. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 265 | 0.4448 | 0.4154 |
| rnafold | ok | 265 | 0.3739 | 0.3592 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | -0.3381 | -0.4049 |
| seed_p | 61 | -0.6142 | -0.7024 |
| seed_p_vs_seed_pars | 31 | -0.5375 | -0.6509 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
