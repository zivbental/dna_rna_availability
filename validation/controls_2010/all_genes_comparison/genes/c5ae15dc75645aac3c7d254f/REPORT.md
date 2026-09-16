# YPR004C
Status: ok. Length: 1149 nt. Measured usable bases: 729. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 729 | 0.3970 | 0.3947 |
| rnafold | ok | 729 | 0.3483 | 0.3516 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 406 | -0.0472 | 0.0190 |
| seed_p | 406 | -0.1747 | -0.2107 |
| seed_p_vs_seed_pars | 269 | -0.1858 | -0.2429 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
