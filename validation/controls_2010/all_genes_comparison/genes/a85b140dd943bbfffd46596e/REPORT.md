# YGL054C
Status: ok. Length: 502 nt. Measured usable bases: 389. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 389 | 0.2190 | 0.2126 |
| rnafold | ok | 389 | 0.1961 | 0.1957 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 339 | -0.1090 | 0.2973 |
| seed_p | 339 | -0.3441 | -0.2229 |
| seed_p_vs_seed_pars | 299 | -0.4957 | -0.3833 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
