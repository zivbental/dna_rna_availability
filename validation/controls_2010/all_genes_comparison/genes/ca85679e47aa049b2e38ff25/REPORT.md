# YDR309C
Status: ok. Length: 1221 nt. Measured usable bases: 723. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 723 | 0.2581 | 0.2715 |
| rnafold | ok | 723 | 0.2099 | 0.2270 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 298 | 0.0430 | -0.3042 |
| seed_p | 298 | -0.3192 | -0.3896 |
| seed_p_vs_seed_pars | 249 | -0.4203 | -0.4466 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
