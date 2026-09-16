# YDR101C
Status: ok. Length: 1884 nt. Measured usable bases: 1298. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1298 | 0.2760 | 0.2653 |
| rnafold | ok | 1298 | 0.2189 | 0.2040 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 688 | -0.0323 | -0.0514 |
| seed_p | 688 | -0.1659 | -0.0821 |
| seed_p_vs_seed_pars | 500 | -0.3031 | -0.1931 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
