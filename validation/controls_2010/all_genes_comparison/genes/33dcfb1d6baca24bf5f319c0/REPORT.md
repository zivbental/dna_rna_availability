# YCR030C
Status: ok. Length: 2828 nt. Measured usable bases: 1386. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1386 | 0.2705 | 0.2578 |
| rnafold | ok | 1386 | 0.2226 | 0.2196 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 258 | 0.0103 | -0.2224 |
| seed_p | 258 | 0.0974 | 0.0633 |
| seed_p_vs_seed_pars | 202 | 0.0920 | 0.0621 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
