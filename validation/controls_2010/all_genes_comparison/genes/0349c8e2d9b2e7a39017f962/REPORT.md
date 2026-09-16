# YGL181W
Status: ok. Length: 1357 nt. Measured usable bases: 654. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 654 | 0.2714 | 0.2698 |
| rnafold | ok | 654 | 0.2085 | 0.2147 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 128 | -0.0450 | 0.0203 |
| seed_p | 128 | 0.4368 | 0.3754 |
| seed_p_vs_seed_pars | 80 | 0.5731 | 0.5656 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
