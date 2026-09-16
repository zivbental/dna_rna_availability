# YCR044C
Status: ok. Length: 1194 nt. Measured usable bases: 758. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 758 | 0.2797 | 0.2695 |
| rnafold | ok | 758 | 0.2057 | 0.2012 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 458 | 0.0714 | 0.1795 |
| seed_p | 458 | 0.0105 | 0.0164 |
| seed_p_vs_seed_pars | 343 | -0.0520 | -0.0807 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
