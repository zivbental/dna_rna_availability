# YHR193C
Status: ok. Length: 587 nt. Measured usable bases: 499. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 499 | 0.3414 | 0.3428 |
| rnafold | ok | 499 | 0.3053 | 0.3217 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 482 | -0.1838 | 0.0325 |
| seed_p | 482 | -0.3628 | -0.0768 |
| seed_p_vs_seed_pars | 469 | -0.3921 | -0.0197 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
