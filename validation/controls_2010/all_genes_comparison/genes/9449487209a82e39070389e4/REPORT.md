# YDL205C
Status: ok. Length: 1274 nt. Measured usable bases: 623. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 623 | 0.3941 | 0.3902 |
| rnafold | ok | 623 | 0.2698 | 0.2548 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 159 | -0.3204 | -0.6405 |
| seed_p | 159 | -0.4550 | -0.5689 |
| seed_p_vs_seed_pars | 105 | -0.6013 | -0.6816 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
