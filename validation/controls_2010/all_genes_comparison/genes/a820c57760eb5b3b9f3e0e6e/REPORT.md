# YOL073C
Status: ok. Length: 1048 nt. Measured usable bases: 707. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 707 | 0.3039 | 0.3121 |
| rnafold | ok | 707 | 0.2498 | 0.2615 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 332 | -0.1618 | -0.4274 |
| seed_p | 332 | -0.5443 | -0.5613 |
| seed_p_vs_seed_pars | 268 | -0.5170 | -0.6676 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
