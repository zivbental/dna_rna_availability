# YLR209C
Status: ok. Length: 1019 nt. Measured usable bases: 622. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 622 | 0.2909 | 0.2857 |
| rnafold | ok | 622 | 0.2618 | 0.2663 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 303 | 0.1846 | 0.0960 |
| seed_p | 303 | -0.1012 | -0.1418 |
| seed_p_vs_seed_pars | 251 | -0.2748 | -0.3416 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
