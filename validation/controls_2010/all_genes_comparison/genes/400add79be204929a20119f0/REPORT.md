# YIR015W
Status: ok. Length: 435 nt. Measured usable bases: 163. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 163 | 0.4115 | 0.3916 |
| rnafold | ok | 163 | 0.3900 | 0.3539 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 22 | -0.7182 | -0.6853 |
| seed_p | 22 | 0.5833 | 0.7295 |
| seed_p_vs_seed_pars | 22 | 0.9763 | 0.7679 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
