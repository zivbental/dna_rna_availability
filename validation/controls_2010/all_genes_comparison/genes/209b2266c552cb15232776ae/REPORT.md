# YBR214W
Status: ok. Length: 1848 nt. Measured usable bases: 873. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 873 | 0.2489 | 0.2344 |
| rnafold | ok | 873 | 0.2100 | 0.2062 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 179 | -0.3236 | -0.0802 |
| seed_p | 179 | -0.6329 | -0.4712 |
| seed_p_vs_seed_pars | 120 | -0.7423 | -0.6247 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
