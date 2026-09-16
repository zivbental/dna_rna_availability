# YGR172C
Status: ok. Length: 894 nt. Measured usable bases: 650. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 650 | 0.2653 | 0.2490 |
| rnafold | ok | 650 | 0.2212 | 0.2321 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 409 | -0.2507 | -0.0821 |
| seed_p | 409 | -0.1628 | -0.2246 |
| seed_p_vs_seed_pars | 297 | -0.2134 | -0.1419 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
