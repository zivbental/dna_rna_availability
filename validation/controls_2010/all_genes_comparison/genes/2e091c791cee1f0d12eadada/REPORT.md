# YMR055C
Status: ok. Length: 1115 nt. Measured usable bases: 411. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 411 | 0.4113 | 0.3916 |
| rnafold | ok | 411 | 0.3715 | 0.3581 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | 0.7756 | 0.6837 |
| seed_p | 25 | 0.8804 | 0.7404 |
| seed_p_vs_seed_pars | 15 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
