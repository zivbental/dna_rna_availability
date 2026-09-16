# YBR160W
Status: ok. Length: 1054 nt. Measured usable bases: 592. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 592 | 0.3257 | 0.3169 |
| rnafold | ok | 592 | 0.2393 | 0.2327 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 166 | -0.2978 | -0.3419 |
| seed_p | 166 | -0.4540 | -0.5831 |
| seed_p_vs_seed_pars | 129 | -0.4614 | -0.5964 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
