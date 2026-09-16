# YLR285W
Status: ok. Length: 1026 nt. Measured usable bases: 530. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 530 | 0.2272 | 0.2056 |
| rnafold | ok | 530 | 0.2169 | 0.2109 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 174 | 0.2686 | 0.2538 |
| seed_p | 174 | 0.0611 | 0.1504 |
| seed_p_vs_seed_pars | 126 | -0.1606 | -0.0090 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
