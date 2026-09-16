# YJR016C
Status: ok. Length: 1910 nt. Measured usable bases: 1586. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1586 | 0.3762 | 0.3665 |
| rnafold | ok | 1586 | 0.2949 | 0.2952 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1523 | -0.0414 | -0.1786 |
| seed_p | 1523 | -0.1447 | -0.2381 |
| seed_p_vs_seed_pars | 1329 | -0.3824 | -0.3956 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
