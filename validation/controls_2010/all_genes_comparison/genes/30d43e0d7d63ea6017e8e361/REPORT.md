# YJR009C
Status: ok. Length: 1129 nt. Measured usable bases: 254. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 254 | 0.2555 | 0.2297 |
| rnafold | ok | 254 | 0.2383 | 0.2035 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 134 | -0.4490 | -0.5972 |
| seed_p | 134 | -0.5354 | -0.5203 |
| seed_p_vs_seed_pars | 116 | -0.5262 | -0.5157 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
