# YLR120C
Status: ok. Length: 2181 nt. Measured usable bases: 1200. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1200 | 0.3300 | 0.3163 |
| rnafold | ok | 1200 | 0.2950 | 0.2722 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 317 | -0.0162 | -0.0303 |
| seed_p | 317 | -0.0520 | -0.1257 |
| seed_p_vs_seed_pars | 243 | -0.0575 | -0.1366 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
