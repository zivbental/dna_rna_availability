# YPL096C-A
Status: ok. Length: 321 nt. Measured usable bases: 176. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 176 | 0.2087 | 0.2084 |
| rnafold | ok | 176 | 0.1607 | 0.1521 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | -0.5009 | -0.4377 |
| seed_p | 60 | -0.3927 | -0.5784 |
| seed_p_vs_seed_pars | 38 | -0.4709 | -0.6121 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
