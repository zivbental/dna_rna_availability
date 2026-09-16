# YBR093C
Status: ok. Length: 1488 nt. Measured usable bases: 745. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 745 | 0.2553 | 0.2573 |
| rnafold | ok | 745 | 0.2618 | 0.2552 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 368 | 0.0189 | 0.0917 |
| seed_p | 368 | -0.2651 | -0.1232 |
| seed_p_vs_seed_pars | 272 | 0.0107 | 0.0674 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
