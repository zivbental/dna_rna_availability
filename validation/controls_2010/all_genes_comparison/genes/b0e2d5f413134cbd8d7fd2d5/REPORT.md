# YPL011C
Status: ok. Length: 1188 nt. Measured usable bases: 417. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 417 | 0.3046 | 0.3094 |
| rnafold | ok | 417 | 0.3185 | 0.3138 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 21 | -0.8148 | -0.8649 |
| seed_p | 21 | -0.6353 | -0.8421 |
| seed_p_vs_seed_pars | 16 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
