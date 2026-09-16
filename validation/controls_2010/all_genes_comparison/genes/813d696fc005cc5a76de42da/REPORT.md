# YGR229C
Status: ok. Length: 1947 nt. Measured usable bases: 899. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 899 | 0.3515 | 0.3345 |
| rnafold | ok | 899 | 0.2805 | 0.2730 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 220 | -0.0917 | 0.0933 |
| seed_p | 220 | -0.1821 | -0.1571 |
| seed_p_vs_seed_pars | 169 | -0.0698 | -0.0645 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
