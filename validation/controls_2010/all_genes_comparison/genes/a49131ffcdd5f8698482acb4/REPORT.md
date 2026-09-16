# YGL231C
Status: ok. Length: 630 nt. Measured usable bases: 456. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 456 | 0.3063 | 0.3208 |
| rnafold | ok | 456 | 0.3486 | 0.3513 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 307 | 0.0964 | 0.0239 |
| seed_p | 307 | -0.1009 | -0.0927 |
| seed_p_vs_seed_pars | 220 | -0.2709 | -0.1016 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
