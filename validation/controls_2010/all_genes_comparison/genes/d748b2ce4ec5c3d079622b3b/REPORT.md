# YBR242W
Status: ok. Length: 932 nt. Measured usable bases: 459. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 459 | 0.4343 | 0.4193 |
| rnafold | ok | 459 | 0.3816 | 0.3834 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 124 | -0.0597 | -0.0991 |
| seed_p | 124 | -0.7420 | -0.7056 |
| seed_p_vs_seed_pars | 99 | -0.6743 | -0.6567 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
