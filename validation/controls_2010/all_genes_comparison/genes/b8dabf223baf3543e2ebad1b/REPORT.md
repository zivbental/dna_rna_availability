# YBR166C
Status: ok. Length: 1490 nt. Measured usable bases: 630. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 630 | 0.2999 | 0.2956 |
| rnafold | ok | 630 | 0.1586 | 0.1646 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | -0.4556 | -0.6803 |
| seed_p | 46 | -0.2105 | -0.1537 |
| seed_p_vs_seed_pars | 38 | -0.5623 | -0.3608 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
