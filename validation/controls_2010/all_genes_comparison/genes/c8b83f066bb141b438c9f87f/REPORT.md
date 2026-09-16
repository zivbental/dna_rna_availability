# YGR203W
Status: ok. Length: 962 nt. Measured usable bases: 302. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 302 | 0.2838 | 0.2722 |
| rnafold | ok | 302 | 0.2461 | 0.2376 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | -0.4303 | -0.6397 |
| seed_p | 25 | -0.7452 | -0.5947 |
| seed_p_vs_seed_pars | 17 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
