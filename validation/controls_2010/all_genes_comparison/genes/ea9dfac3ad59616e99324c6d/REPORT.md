# YBR172C
Status: ok. Length: 2430 nt. Measured usable bases: 1061. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1061 | 0.3415 | 0.3240 |
| rnafold | ok | 1061 | 0.2984 | 0.2829 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 169 | -0.0546 | -0.1931 |
| seed_p | 169 | -0.3847 | -0.3448 |
| seed_p_vs_seed_pars | 123 | -0.6384 | -0.5641 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
