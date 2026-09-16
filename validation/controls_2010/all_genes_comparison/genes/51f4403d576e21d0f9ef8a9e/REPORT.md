# YER147C
Status: ok. Length: 1968 nt. Measured usable bases: 759. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 759 | 0.3660 | 0.3455 |
| rnafold | ok | 759 | 0.2849 | 0.2748 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | 0.1575 | 0.2404 |
| seed_p | 65 | -0.0068 | 0.4929 |
| seed_p_vs_seed_pars | 39 | -0.8152 | -0.6671 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
