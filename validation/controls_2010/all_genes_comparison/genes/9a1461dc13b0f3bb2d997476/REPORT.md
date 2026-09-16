# YAR003W
Status: ok. Length: 1806 nt. Measured usable bases: 885. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 885 | 0.3444 | 0.3357 |
| rnafold | ok | 885 | 0.3134 | 0.3163 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 253 | -0.0411 | -0.1154 |
| seed_p | 253 | 0.0326 | 0.1164 |
| seed_p_vs_seed_pars | 151 | -0.1511 | -0.1963 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
