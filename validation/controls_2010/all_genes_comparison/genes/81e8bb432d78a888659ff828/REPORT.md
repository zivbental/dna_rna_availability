# YGR044C
Status: ok. Length: 1119 nt. Measured usable bases: 701. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 701 | 0.3045 | 0.2987 |
| rnafold | ok | 701 | 0.2641 | 0.2629 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 296 | -0.3107 | -0.2333 |
| seed_p | 296 | -0.1910 | -0.1899 |
| seed_p_vs_seed_pars | 206 | -0.1914 | -0.3059 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
