# YJL068C
Status: ok. Length: 986 nt. Measured usable bases: 684. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 684 | 0.3410 | 0.3270 |
| rnafold | ok | 684 | 0.3240 | 0.3140 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 457 | -0.1326 | -0.3067 |
| seed_p | 457 | -0.2837 | -0.3665 |
| seed_p_vs_seed_pars | 353 | -0.4033 | -0.3921 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
