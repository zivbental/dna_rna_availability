# YNL264C
Status: ok. Length: 1231 nt. Measured usable bases: 563. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 563 | 0.3998 | 0.3989 |
| rnafold | ok | 563 | 0.2067 | 0.2513 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 78 | -0.5726 | -0.4724 |
| seed_p | 78 | -0.4644 | -0.3991 |
| seed_p_vs_seed_pars | 49 | -0.5691 | -0.5888 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
