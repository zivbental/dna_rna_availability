# YOL031C
Status: ok. Length: 1352 nt. Measured usable bases: 596. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 596 | 0.2665 | 0.2442 |
| rnafold | ok | 596 | 0.2193 | 0.2072 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 95 | -0.1709 | -0.6430 |
| seed_p | 95 | -0.4602 | -0.5213 |
| seed_p_vs_seed_pars | 42 | -0.2033 | -0.1973 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
