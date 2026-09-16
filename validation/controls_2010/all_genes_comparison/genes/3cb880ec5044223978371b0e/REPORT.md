# YER113C
Status: ok. Length: 2121 nt. Measured usable bases: 967. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 967 | 0.3153 | 0.2947 |
| rnafold | ok | 967 | 0.2237 | 0.2187 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 166 | -0.0527 | -0.3597 |
| seed_p | 166 | -0.0637 | -0.3664 |
| seed_p_vs_seed_pars | 123 | -0.2107 | -0.4100 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
