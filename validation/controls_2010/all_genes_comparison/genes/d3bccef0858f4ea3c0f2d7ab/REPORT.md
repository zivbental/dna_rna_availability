# YNL200C
Status: ok. Length: 902 nt. Measured usable bases: 489. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 489 | 0.2998 | 0.2761 |
| rnafold | ok | 489 | 0.2069 | 0.2051 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 172 | -0.3266 | -0.3022 |
| seed_p | 172 | -0.2401 | -0.2502 |
| seed_p_vs_seed_pars | 147 | -0.5074 | -0.5040 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
