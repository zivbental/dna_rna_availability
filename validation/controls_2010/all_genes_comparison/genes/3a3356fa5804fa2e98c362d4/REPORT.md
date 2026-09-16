# YNL302C
Status: ok. Length: 545 nt. Measured usable bases: 242. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 242 | 0.3900 | 0.3848 |
| rnafold | ok | 242 | 0.1948 | 0.1985 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 96 | -0.1087 | -0.3055 |
| seed_p | 96 | -0.4383 | -0.4976 |
| seed_p_vs_seed_pars | 71 | -0.5000 | -0.3187 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
