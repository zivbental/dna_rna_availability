# YCR037C
Status: ok. Length: 2772 nt. Measured usable bases: 1179. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1179 | 0.3582 | 0.3329 |
| rnafold | ok | 1179 | 0.3023 | 0.2813 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 59 | -0.1525 | -0.1543 |
| seed_p | 59 | -0.6307 | -0.5164 |
| seed_p_vs_seed_pars | 48 | -0.2788 | -0.3216 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
