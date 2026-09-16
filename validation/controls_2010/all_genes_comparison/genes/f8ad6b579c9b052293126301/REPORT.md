# YCR094W
Status: ok. Length: 1311 nt. Measured usable bases: 486. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 486 | 0.3389 | 0.3376 |
| rnafold | ok | 486 | 0.3657 | 0.3632 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | 0.0775 | -0.3370 |
| seed_p | 46 | -0.3016 | -0.3005 |
| seed_p_vs_seed_pars | 35 | -0.4686 | -0.5083 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
