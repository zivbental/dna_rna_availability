# YKL052C
Status: ok. Length: 929 nt. Measured usable bases: 409. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 409 | 0.3410 | 0.3449 |
| rnafold | ok | 409 | 0.3307 | 0.3253 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | -0.3810 | -0.6013 |
| seed_p | 54 | -0.2909 | -0.2844 |
| seed_p_vs_seed_pars | 42 | -0.6601 | -0.5464 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
