# YLR220W
Status: ok. Length: 1134 nt. Measured usable bases: 693. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 693 | 0.4434 | 0.4261 |
| rnafold | ok | 693 | 0.4202 | 0.4050 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 216 | -0.1214 | -0.0874 |
| seed_p | 216 | -0.2420 | -0.3089 |
| seed_p_vs_seed_pars | 171 | -0.3975 | -0.5044 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
