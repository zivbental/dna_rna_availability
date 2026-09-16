# YDR016C
Status: ok. Length: 387 nt. Measured usable bases: 225. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 225 | 0.3646 | 0.3498 |
| rnafold | ok | 225 | 0.3073 | 0.3005 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 84 | -0.2817 | -0.3849 |
| seed_p | 84 | -0.7476 | -0.6076 |
| seed_p_vs_seed_pars | 57 | -0.5832 | -0.4854 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
