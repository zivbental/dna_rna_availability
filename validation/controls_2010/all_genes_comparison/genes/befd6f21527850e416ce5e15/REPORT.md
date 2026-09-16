# YIR026C
Status: ok. Length: 1193 nt. Measured usable bases: 612. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 612 | 0.3221 | 0.3200 |
| rnafold | ok | 612 | 0.3521 | 0.3392 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 127 | -0.1716 | -0.1995 |
| seed_p | 127 | -0.2065 | -0.2022 |
| seed_p_vs_seed_pars | 80 | -0.4418 | -0.3443 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
