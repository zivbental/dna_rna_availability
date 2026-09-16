# YOR086C
Status: ok. Length: 3858 nt. Measured usable bases: 2054. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2054 | 0.2949 | 0.2826 |
| rnafold | ok | 2054 | 0.1948 | 0.1933 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 643 | -0.0443 | -0.1060 |
| seed_p | 643 | -0.1939 | -0.1721 |
| seed_p_vs_seed_pars | 443 | -0.3475 | -0.3347 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
