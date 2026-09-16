# YKL166C
Status: ok. Length: 1386 nt. Measured usable bases: 674. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 674 | 0.4246 | 0.4318 |
| rnafold | ok | 674 | 0.3466 | 0.3478 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 123 | -0.1828 | -0.6417 |
| seed_p | 123 | -0.2936 | -0.3810 |
| seed_p_vs_seed_pars | 103 | -0.4583 | -0.4304 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
