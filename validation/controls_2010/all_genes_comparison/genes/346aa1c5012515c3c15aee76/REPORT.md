# YPL015C
Status: ok. Length: 1421 nt. Measured usable bases: 938. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 938 | 0.3114 | 0.2908 |
| rnafold | ok | 938 | 0.2780 | 0.2467 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 421 | -0.0960 | 0.1022 |
| seed_p | 421 | -0.0348 | 0.0993 |
| seed_p_vs_seed_pars | 294 | -0.0437 | -0.0156 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
