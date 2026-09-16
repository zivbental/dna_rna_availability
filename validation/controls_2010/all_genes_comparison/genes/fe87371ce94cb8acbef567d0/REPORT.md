# YGL147C
Status: ok. Length: 692 nt. Measured usable bases: 359. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 359 | 0.2866 | 0.2933 |
| rnafold | ok | 359 | 0.3033 | 0.3050 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 222 | -0.1541 | -0.1099 |
| seed_p | 222 | -0.3740 | -0.3635 |
| seed_p_vs_seed_pars | 201 | -0.5073 | -0.5542 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
