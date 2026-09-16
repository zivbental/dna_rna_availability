# YHL020C
Status: ok. Length: 1390 nt. Measured usable bases: 753. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 753 | 0.3230 | 0.3173 |
| rnafold | ok | 753 | 0.2805 | 0.2872 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 256 | 0.1326 | 0.0743 |
| seed_p | 256 | 0.0257 | 0.0536 |
| seed_p_vs_seed_pars | 209 | -0.2311 | -0.1441 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
