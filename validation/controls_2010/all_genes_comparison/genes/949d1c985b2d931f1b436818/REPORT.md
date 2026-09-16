# YHR169W
Status: ok. Length: 1517 nt. Measured usable bases: 794. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 794 | 0.4622 | 0.4585 |
| rnafold | ok | 794 | 0.2907 | 0.2856 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 148 | -0.3539 | -0.6012 |
| seed_p | 148 | -0.3332 | -0.2733 |
| seed_p_vs_seed_pars | 122 | -0.4889 | -0.3407 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
