# YDL072C
Status: ok. Length: 732 nt. Measured usable bases: 575. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 575 | 0.2477 | 0.2591 |
| rnafold | ok | 575 | 0.2186 | 0.2434 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 494 | -0.0448 | 0.0492 |
| seed_p | 494 | -0.0897 | -0.1050 |
| seed_p_vs_seed_pars | 400 | -0.0748 | -0.1170 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
