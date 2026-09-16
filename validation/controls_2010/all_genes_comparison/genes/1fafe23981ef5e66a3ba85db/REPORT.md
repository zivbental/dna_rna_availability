# YJL196C
Status: ok. Length: 1088 nt. Measured usable bases: 785. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 785 | 0.3291 | 0.3059 |
| rnafold | ok | 785 | 0.3180 | 0.2938 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 576 | 0.1205 | 0.0999 |
| seed_p | 576 | 0.0512 | 0.0686 |
| seed_p_vs_seed_pars | 430 | 0.0043 | -0.0656 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
