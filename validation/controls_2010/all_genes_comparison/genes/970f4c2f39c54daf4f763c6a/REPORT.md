# YCL001W
Status: ok. Length: 673 nt. Measured usable bases: 417. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 417 | 0.2991 | 0.3070 |
| rnafold | ok | 417 | 0.2707 | 0.2652 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 216 | -0.1439 | -0.1425 |
| seed_p | 216 | -0.1940 | -0.3204 |
| seed_p_vs_seed_pars | 194 | -0.2483 | -0.2686 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
