# YDR140W
Status: ok. Length: 802 nt. Measured usable bases: 386. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 386 | 0.2216 | 0.2311 |
| rnafold | ok | 386 | 0.1479 | 0.1571 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 50 | -0.0160 | -0.4835 |
| seed_p | 50 | -0.3441 | -0.4991 |
| seed_p_vs_seed_pars | 39 | -0.2148 | -0.1219 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
