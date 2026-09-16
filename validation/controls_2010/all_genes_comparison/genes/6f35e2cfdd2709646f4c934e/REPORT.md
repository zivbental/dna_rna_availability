# YKL213C
Status: ok. Length: 2237 nt. Measured usable bases: 975. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 975 | 0.3211 | 0.3183 |
| rnafold | ok | 975 | 0.2799 | 0.2864 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 125 | -0.1273 | -0.0262 |
| seed_p | 125 | 0.2353 | 0.2617 |
| seed_p_vs_seed_pars | 64 | -0.2135 | -0.0175 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
