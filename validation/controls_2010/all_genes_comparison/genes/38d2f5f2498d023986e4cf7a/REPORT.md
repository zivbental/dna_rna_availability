# YER126C
Status: ok. Length: 935 nt. Measured usable bases: 535. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 535 | 0.2924 | 0.3389 |
| rnafold | ok | 535 | 0.2424 | 0.2742 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 180 | 0.2403 | 0.3423 |
| seed_p | 180 | 0.0209 | -0.0205 |
| seed_p_vs_seed_pars | 154 | 0.1112 | 0.1049 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
