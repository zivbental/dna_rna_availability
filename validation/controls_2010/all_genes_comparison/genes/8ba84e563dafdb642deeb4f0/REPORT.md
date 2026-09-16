# YKL025C
Status: ok. Length: 2082 nt. Measured usable bases: 763. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 763 | 0.2756 | 0.2671 |
| rnafold | ok | 763 | 0.2582 | 0.2437 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 45 | -0.0207 | -0.2956 |
| seed_p | 45 | 0.0947 | 0.1900 |
| seed_p_vs_seed_pars | 32 | -0.6506 | -0.4547 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
