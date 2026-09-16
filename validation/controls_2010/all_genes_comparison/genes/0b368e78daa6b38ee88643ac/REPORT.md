# YMR013C
Status: ok. Length: 1844 nt. Measured usable bases: 602. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 602 | 0.1824 | 0.1802 |
| rnafold | ok | 602 | 0.1793 | 0.1737 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 49 | -0.2175 | -0.5693 |
| seed_p | 49 | -0.0561 | -0.4173 |
| seed_p_vs_seed_pars | 48 | 0.3423 | -0.3198 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
