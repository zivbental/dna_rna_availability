# YJR116W
Status: ok. Length: 1189 nt. Measured usable bases: 487. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 487 | 0.1836 | 0.1766 |
| rnafold | ok | 487 | 0.2489 | 0.2178 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | 0.4567 | 0.4332 |
| seed_p | 65 | -0.0558 | 0.0454 |
| seed_p_vs_seed_pars | 45 | 0.0102 | 0.2992 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
