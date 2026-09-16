# YLR259C
Status: ok. Length: 1826 nt. Measured usable bases: 1557. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1557 | 0.2875 | 0.2843 |
| rnafold | ok | 1557 | 0.2273 | 0.2442 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1480 | -0.0960 | -0.2085 |
| seed_p | 1480 | -0.0637 | -0.1842 |
| seed_p_vs_seed_pars | 1277 | -0.1737 | -0.1951 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
