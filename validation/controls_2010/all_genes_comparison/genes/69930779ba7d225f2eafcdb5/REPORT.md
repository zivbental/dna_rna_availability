# YPL246C
Status: ok. Length: 980 nt. Measured usable bases: 700. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 700 | 0.2169 | 0.2238 |
| rnafold | ok | 700 | 0.1830 | 0.1890 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 485 | 0.0556 | 0.2020 |
| seed_p | 485 | -0.0500 | -0.0066 |
| seed_p_vs_seed_pars | 383 | -0.2030 | -0.1513 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
