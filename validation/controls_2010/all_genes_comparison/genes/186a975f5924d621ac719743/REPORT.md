# YER073W
Status: ok. Length: 1872 nt. Measured usable bases: 1083. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1083 | 0.2915 | 0.2739 |
| rnafold | ok | 1083 | 0.2013 | 0.1861 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 377 | -0.1700 | -0.0678 |
| seed_p | 377 | -0.0884 | -0.0776 |
| seed_p_vs_seed_pars | 298 | -0.2098 | -0.2006 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
