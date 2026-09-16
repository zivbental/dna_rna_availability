# YOR270C
Status: ok. Length: 2792 nt. Measured usable bases: 2334. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2334 | 0.2994 | 0.2824 |
| rnafold | ok | 2334 | 0.2116 | 0.2071 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2094 | 0.0387 | 0.0074 |
| seed_p | 2094 | -0.0874 | -0.0871 |
| seed_p_vs_seed_pars | 1659 | -0.2111 | -0.1749 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
