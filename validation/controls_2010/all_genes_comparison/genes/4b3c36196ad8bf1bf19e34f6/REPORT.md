# YPL013C
Status: ok. Length: 528 nt. Measured usable bases: 222. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 222 | 0.2965 | 0.2724 |
| rnafold | ok | 222 | 0.3085 | 0.2734 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | -0.0240 | 0.1607 |
| seed_p | 51 | -0.1996 | -0.3849 |
| seed_p_vs_seed_pars | 33 | -0.1990 | -0.4577 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
