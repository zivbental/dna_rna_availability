# YIL075C
Status: ok. Length: 2966 nt. Measured usable bases: 2025. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2025 | 0.2876 | 0.2760 |
| rnafold | ok | 2025 | 0.2917 | 0.2867 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1066 | -0.1126 | -0.0357 |
| seed_p | 1066 | -0.1332 | -0.0749 |
| seed_p_vs_seed_pars | 814 | -0.0998 | -0.1033 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
