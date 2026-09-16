# YDL188C
Status: ok. Length: 1380 nt. Measured usable bases: 633. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 633 | 0.2761 | 0.2806 |
| rnafold | ok | 633 | 0.2518 | 0.2732 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 223 | 0.2869 | -0.0416 |
| seed_p | 223 | -0.0783 | -0.0860 |
| seed_p_vs_seed_pars | 180 | -0.2115 | -0.1970 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
