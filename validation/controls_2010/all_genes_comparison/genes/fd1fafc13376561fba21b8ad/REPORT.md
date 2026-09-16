# YBL045C
Status: ok. Length: 1733 nt. Measured usable bases: 1173. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1173 | 0.3069 | 0.3046 |
| rnafold | ok | 1173 | 0.2670 | 0.2651 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 620 | 0.1074 | 0.1115 |
| seed_p | 620 | 0.0825 | 0.1988 |
| seed_p_vs_seed_pars | 521 | -0.3140 | -0.1647 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
