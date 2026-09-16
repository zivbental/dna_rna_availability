# YBR283C
Status: ok. Length: 1760 nt. Measured usable bases: 1499. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1499 | 0.3082 | 0.2992 |
| rnafold | ok | 1499 | 0.2760 | 0.2676 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1359 | 0.0545 | -0.1015 |
| seed_p | 1359 | -0.1106 | -0.1606 |
| seed_p_vs_seed_pars | 1199 | -0.2239 | -0.1936 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
