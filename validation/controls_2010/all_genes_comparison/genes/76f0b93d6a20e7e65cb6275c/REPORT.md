# YJR045C
Status: ok. Length: 2302 nt. Measured usable bases: 1955. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1955 | 0.3186 | 0.3002 |
| rnafold | ok | 1955 | 0.2709 | 0.2673 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1831 | -0.1809 | -0.1365 |
| seed_p | 1831 | -0.2132 | -0.1488 |
| seed_p_vs_seed_pars | 1589 | -0.2765 | -0.2051 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
