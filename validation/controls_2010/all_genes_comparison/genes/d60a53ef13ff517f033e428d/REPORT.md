# YLR268W
Status: ok. Length: 800 nt. Measured usable bases: 541. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 541 | 0.3675 | 0.3656 |
| rnafold | ok | 541 | 0.3006 | 0.3076 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 289 | -0.2069 | -0.2657 |
| seed_p | 289 | -0.3312 | -0.4385 |
| seed_p_vs_seed_pars | 181 | -0.1984 | -0.3199 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
