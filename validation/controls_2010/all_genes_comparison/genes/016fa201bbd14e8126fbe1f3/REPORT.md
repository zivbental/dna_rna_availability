# YPL210C
Status: ok. Length: 2088 nt. Measured usable bases: 832. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 832 | 0.3839 | 0.3781 |
| rnafold | ok | 832 | 0.3290 | 0.3303 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.8451 | -0.6085 |
| seed_p | 58 | -0.8273 | -0.8267 |
| seed_p_vs_seed_pars | 27 | -0.6502 | -0.5835 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
