# YMR260C
Status: ok. Length: 616 nt. Measured usable bases: 459. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 459 | 0.4034 | 0.4144 |
| rnafold | ok | 459 | 0.2933 | 0.3016 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 377 | -0.1307 | 0.0118 |
| seed_p | 377 | -0.2642 | -0.3235 |
| seed_p_vs_seed_pars | 319 | -0.3931 | -0.4661 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
