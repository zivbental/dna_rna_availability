# YER048C
Status: ok. Length: 1344 nt. Measured usable bases: 648. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 648 | 0.3185 | 0.3039 |
| rnafold | ok | 648 | 0.3031 | 0.2891 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 116 | -0.1224 | 0.1526 |
| seed_p | 116 | -0.0435 | -0.0680 |
| seed_p_vs_seed_pars | 82 | 0.3161 | 0.2320 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
