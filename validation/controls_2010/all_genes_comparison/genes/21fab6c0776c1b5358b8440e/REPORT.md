# YEL016C
Status: ok. Length: 1722 nt. Measured usable bases: 734. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 734 | 0.2839 | 0.2899 |
| rnafold | ok | 734 | 0.2696 | 0.2858 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | 0.2355 | 0.0224 |
| seed_p | 72 | 0.2809 | 0.2238 |
| seed_p_vs_seed_pars | 35 | 0.6446 | 0.7996 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
