# YGL078C
Status: ok. Length: 1818 nt. Measured usable bases: 863. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 863 | 0.2852 | 0.2759 |
| rnafold | ok | 863 | 0.2056 | 0.1842 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 284 | 0.1990 | 0.2913 |
| seed_p | 284 | -0.0217 | 0.1182 |
| seed_p_vs_seed_pars | 198 | 0.1555 | 0.2033 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
