# YBR111C
Status: ok. Length: 779 nt. Measured usable bases: 590. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 590 | 0.3214 | 0.3074 |
| rnafold | ok | 590 | 0.2802 | 0.2577 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 465 | -0.2005 | 0.0857 |
| seed_p | 465 | -0.2483 | 0.0520 |
| seed_p_vs_seed_pars | 379 | -0.3089 | -0.0739 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
