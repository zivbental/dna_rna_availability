# YLR091W
Status: ok. Length: 1224 nt. Measured usable bases: 513. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 513 | 0.2079 | 0.2234 |
| rnafold | ok | 513 | 0.1875 | 0.2151 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 28 | -0.7467 | -0.8172 |
| seed_p | 28 | -0.6367 | -0.7535 |
| seed_p_vs_seed_pars | 25 | -0.7215 | -0.6489 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
