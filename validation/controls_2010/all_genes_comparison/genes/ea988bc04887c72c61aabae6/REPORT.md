# YER105C
Status: ok. Length: 4434 nt. Measured usable bases: 1990. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1990 | 0.3063 | 0.2906 |
| rnafold | ok | 1990 | 0.2883 | 0.2770 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 288 | -0.1253 | 0.1694 |
| seed_p | 288 | 0.1952 | -0.0457 |
| seed_p_vs_seed_pars | 193 | -0.0592 | -0.2073 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
