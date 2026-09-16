# YLR276C
Status: ok. Length: 1978 nt. Measured usable bases: 723. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 723 | 0.3191 | 0.3123 |
| rnafold | ok | 723 | 0.3039 | 0.2924 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 64 | -0.6339 | -0.6913 |
| seed_p | 64 | -0.8958 | -0.8343 |
| seed_p_vs_seed_pars | 50 | -0.8815 | -0.8965 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
