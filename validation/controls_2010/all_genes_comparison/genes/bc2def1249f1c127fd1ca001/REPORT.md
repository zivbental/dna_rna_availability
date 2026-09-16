# YJL200C
Status: ok. Length: 2542 nt. Measured usable bases: 1493. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1493 | 0.3574 | 0.3539 |
| rnafold | ok | 1493 | 0.2840 | 0.2896 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 446 | -0.1465 | -0.2282 |
| seed_p | 446 | -0.1652 | -0.2123 |
| seed_p_vs_seed_pars | 352 | -0.1849 | -0.2354 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
