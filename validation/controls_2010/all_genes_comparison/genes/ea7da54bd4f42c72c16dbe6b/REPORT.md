# YGL169W
Status: ok. Length: 1577 nt. Measured usable bases: 737. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 737 | 0.3175 | 0.3141 |
| rnafold | ok | 737 | 0.2545 | 0.2454 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | -0.3010 | -0.1928 |
| seed_p | 143 | -0.0852 | -0.2339 |
| seed_p_vs_seed_pars | 123 | -0.2185 | -0.3912 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
