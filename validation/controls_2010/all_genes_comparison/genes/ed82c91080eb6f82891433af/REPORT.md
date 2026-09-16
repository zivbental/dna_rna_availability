# YDR333C
Status: ok. Length: 2399 nt. Measured usable bases: 1130. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1130 | 0.3048 | 0.2940 |
| rnafold | ok | 1130 | 0.2747 | 0.2656 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 198 | 0.0554 | 0.1545 |
| seed_p | 198 | 0.0880 | 0.1497 |
| seed_p_vs_seed_pars | 158 | 0.0890 | 0.0208 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
