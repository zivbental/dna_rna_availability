# YJR004C
Status: ok. Length: 2091 nt. Measured usable bases: 1915. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1915 | 0.3190 | 0.2994 |
| rnafold | ok | 1915 | 0.2918 | 0.2866 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1875 | -0.0438 | -0.0961 |
| seed_p | 1875 | -0.1189 | -0.1116 |
| seed_p_vs_seed_pars | 1778 | -0.2836 | -0.2903 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
