# YOR311C
Status: ok. Length: 935 nt. Measured usable bases: 633. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 633 | 0.2080 | 0.1847 |
| rnafold | ok | 633 | 0.1885 | 0.1916 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 302 | -0.0277 | -0.0751 |
| seed_p | 302 | -0.0545 | -0.1742 |
| seed_p_vs_seed_pars | 247 | -0.1647 | -0.2529 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
