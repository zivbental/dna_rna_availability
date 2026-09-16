# YBR087W
Status: ok. Length: 1130 nt. Measured usable bases: 665. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 665 | 0.3236 | 0.3252 |
| rnafold | ok | 665 | 0.3201 | 0.3045 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 196 | 0.0880 | 0.2221 |
| seed_p | 196 | 0.1274 | 0.0956 |
| seed_p_vs_seed_pars | 148 | 0.1112 | -0.0311 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
