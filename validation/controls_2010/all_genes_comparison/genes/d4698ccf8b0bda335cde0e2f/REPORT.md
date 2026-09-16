# YAL021C
Status: ok. Length: 2783 nt. Measured usable bases: 1618. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1618 | 0.3225 | 0.3160 |
| rnafold | ok | 1618 | 0.2932 | 0.2830 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 598 | 0.0219 | 0.0273 |
| seed_p | 598 | -0.0663 | -0.0072 |
| seed_p_vs_seed_pars | 455 | -0.1759 | -0.1745 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
