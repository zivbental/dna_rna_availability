# YEL015W
Status: ok. Length: 1735 nt. Measured usable bases: 844. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 844 | 0.2517 | 0.2520 |
| rnafold | ok | 844 | 0.1822 | 0.1871 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | -0.0256 | -0.0398 |
| seed_p | 101 | -0.3362 | 0.0865 |
| seed_p_vs_seed_pars | 61 | -0.3814 | -0.4526 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
