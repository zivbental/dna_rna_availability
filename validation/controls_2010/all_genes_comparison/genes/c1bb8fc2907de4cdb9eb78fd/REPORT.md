# YAL060W
Status: ok. Length: 1353 nt. Measured usable bases: 864. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 864 | 0.3451 | 0.3228 |
| rnafold | ok | 864 | 0.2907 | 0.2896 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 546 | 0.1332 | 0.1141 |
| seed_p | 546 | -0.1750 | -0.0254 |
| seed_p_vs_seed_pars | 450 | -0.2645 | -0.1290 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
