# YDR249C
Status: ok. Length: 1241 nt. Measured usable bases: 487. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 487 | 0.2146 | 0.1904 |
| rnafold | ok | 487 | 0.1745 | 0.1647 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 40 | -0.2175 | -0.3051 |
| seed_p | 40 | -0.4577 | -0.3715 |
| seed_p_vs_seed_pars | 35 | -0.3395 | -0.2871 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
