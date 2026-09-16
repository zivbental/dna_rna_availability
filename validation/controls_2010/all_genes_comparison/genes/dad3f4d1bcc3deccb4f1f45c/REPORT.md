# YBR069C
Status: ok. Length: 2068 nt. Measured usable bases: 1681. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1681 | 0.3706 | 0.3614 |
| rnafold | ok | 1681 | 0.3109 | 0.2962 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1442 | -0.1061 | -0.2877 |
| seed_p | 1442 | -0.3312 | -0.2821 |
| seed_p_vs_seed_pars | 1176 | -0.4709 | -0.4279 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
