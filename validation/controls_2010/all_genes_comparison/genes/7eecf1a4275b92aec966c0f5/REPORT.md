# YML106W
Status: ok. Length: 1050 nt. Measured usable bases: 885. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 885 | 0.3341 | 0.3229 |
| rnafold | ok | 885 | 0.2898 | 0.2911 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 765 | -0.2013 | -0.1649 |
| seed_p | 765 | -0.3990 | -0.3999 |
| seed_p_vs_seed_pars | 663 | -0.4698 | -0.3560 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
