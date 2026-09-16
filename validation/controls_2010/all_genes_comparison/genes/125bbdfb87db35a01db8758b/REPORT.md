# YGL225W
Status: ok. Length: 1169 nt. Measured usable bases: 963. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 963 | 0.2567 | 0.2566 |
| rnafold | ok | 963 | 0.2323 | 0.2369 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 880 | -0.0634 | 0.0262 |
| seed_p | 880 | -0.1641 | -0.1597 |
| seed_p_vs_seed_pars | 814 | -0.2019 | -0.1682 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
