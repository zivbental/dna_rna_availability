# YJR076C
Status: ok. Length: 1410 nt. Measured usable bases: 693. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 693 | 0.3211 | 0.3158 |
| rnafold | ok | 693 | 0.3359 | 0.3225 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 140 | -0.2159 | -0.0743 |
| seed_p | 140 | -0.0773 | -0.0252 |
| seed_p_vs_seed_pars | 91 | -0.5178 | -0.2581 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
