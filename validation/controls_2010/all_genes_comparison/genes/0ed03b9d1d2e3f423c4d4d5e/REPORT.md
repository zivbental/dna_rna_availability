# YDL015C
Status: ok. Length: 1173 nt. Measured usable bases: 967. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 967 | 0.2725 | 0.2475 |
| rnafold | ok | 967 | 0.2574 | 0.2320 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 877 | -0.0277 | -0.2537 |
| seed_p | 877 | -0.2649 | -0.3196 |
| seed_p_vs_seed_pars | 734 | -0.2673 | -0.2493 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
