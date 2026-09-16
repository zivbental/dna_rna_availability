# YCR024C-A
Status: ok. Length: 123 nt. Measured usable bases: 77. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 77 | 0.5027 | 0.4413 |
| rnafold | ok | 77 | 0.5027 | 0.4413 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | 0.2600 | 0.3631 |
| seed_p | 54 | 0.2775 | 0.4046 |
| seed_p_vs_seed_pars | 45 | 0.2564 | -0.0004 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
