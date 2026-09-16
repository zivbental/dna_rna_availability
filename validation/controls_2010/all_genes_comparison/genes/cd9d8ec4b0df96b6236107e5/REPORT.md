# YDR019C
Status: ok. Length: 1392 nt. Measured usable bases: 701. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 701 | 0.3714 | 0.3662 |
| rnafold | ok | 701 | 0.2808 | 0.2905 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 163 | -0.1401 | -0.4051 |
| seed_p | 163 | -0.4466 | -0.2797 |
| seed_p_vs_seed_pars | 93 | -0.5771 | -0.5878 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
