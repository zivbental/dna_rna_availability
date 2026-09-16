# YDR307W
Status: ok. Length: 2198 nt. Measured usable bases: 861. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 861 | 0.2851 | 0.2644 |
| rnafold | ok | 861 | 0.2739 | 0.2619 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 98 | -0.4246 | -0.5351 |
| seed_p | 98 | -0.7336 | -0.6775 |
| seed_p_vs_seed_pars | 68 | -0.6375 | -0.5853 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
