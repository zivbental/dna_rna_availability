# YLR301W
Status: ok. Length: 897 nt. Measured usable bases: 704. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 704 | 0.2969 | 0.2852 |
| rnafold | ok | 704 | 0.2569 | 0.2551 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 581 | 0.0060 | 0.0329 |
| seed_p | 581 | -0.0634 | -0.0350 |
| seed_p_vs_seed_pars | 468 | -0.1129 | -0.1188 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
