# YOR360C
Status: ok. Length: 1883 nt. Measured usable bases: 1056. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1056 | 0.2813 | 0.2680 |
| rnafold | ok | 1056 | 0.2183 | 0.2210 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 330 | 0.1817 | 0.1501 |
| seed_p | 330 | 0.0094 | 0.0000 |
| seed_p_vs_seed_pars | 222 | 0.0738 | 0.0693 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
