# YEL037C
Status: ok. Length: 1492 nt. Measured usable bases: 1023. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1023 | 0.3361 | 0.3281 |
| rnafold | ok | 1023 | 0.3280 | 0.3297 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 645 | -0.1445 | -0.2785 |
| seed_p | 645 | -0.2246 | -0.2498 |
| seed_p_vs_seed_pars | 500 | -0.3067 | -0.2872 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
