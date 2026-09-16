# YIL164C
Status: ok. Length: 600 nt. Measured usable bases: 214. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 214 | 0.4214 | 0.4303 |
| rnafold | ok | 214 | 0.3854 | 0.4203 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 9 | undefined | undefined |
| seed_p | 9 | undefined | undefined |
| seed_p_vs_seed_pars | 4 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
