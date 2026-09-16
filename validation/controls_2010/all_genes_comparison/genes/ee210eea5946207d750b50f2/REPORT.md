# YIL022W
Status: ok. Length: 1632 nt. Measured usable bases: 981. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 981 | 0.2930 | 0.2747 |
| rnafold | ok | 981 | 0.2160 | 0.2091 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 372 | -0.0631 | 0.1260 |
| seed_p | 372 | -0.3073 | -0.3208 |
| seed_p_vs_seed_pars | 303 | -0.4591 | -0.3447 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
