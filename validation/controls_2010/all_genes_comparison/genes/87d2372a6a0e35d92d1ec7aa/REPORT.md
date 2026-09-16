# YGL213C
Status: ok. Length: 1447 nt. Measured usable bases: 692. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 692 | 0.2115 | 0.2035 |
| rnafold | ok | 692 | 0.1859 | 0.1790 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 163 | 0.2927 | 0.2583 |
| seed_p | 163 | -0.2239 | -0.1712 |
| seed_p_vs_seed_pars | 128 | -0.3959 | -0.3034 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
