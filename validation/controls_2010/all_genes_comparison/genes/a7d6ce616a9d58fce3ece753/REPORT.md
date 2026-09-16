# YJR080C
Status: ok. Length: 1328 nt. Measured usable bases: 508. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 508 | 0.3642 | 0.3586 |
| rnafold | ok | 508 | 0.3088 | 0.3080 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.3258 | -0.3796 |
| seed_p | 58 | -0.7608 | -0.7129 |
| seed_p_vs_seed_pars | 45 | -0.7219 | -0.8914 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
