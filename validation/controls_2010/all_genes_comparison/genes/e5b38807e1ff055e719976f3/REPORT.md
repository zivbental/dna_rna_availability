# YER107C
Status: ok. Length: 1388 nt. Measured usable bases: 838. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 838 | 0.3025 | 0.3025 |
| rnafold | ok | 838 | 0.2044 | 0.2121 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 296 | 0.0082 | -0.0536 |
| seed_p | 296 | -0.1556 | -0.1595 |
| seed_p_vs_seed_pars | 245 | 0.0273 | 0.0459 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
