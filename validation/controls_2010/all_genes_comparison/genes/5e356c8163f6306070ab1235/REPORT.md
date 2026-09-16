# YKL119C
Status: ok. Length: 753 nt. Measured usable bases: 324. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 324 | 0.2651 | 0.2679 |
| rnafold | ok | 324 | 0.2559 | 0.2629 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | 0.3772 | 0.5142 |
| seed_p | 61 | -0.0761 | 0.0097 |
| seed_p_vs_seed_pars | 48 | -0.0367 | -0.0636 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
