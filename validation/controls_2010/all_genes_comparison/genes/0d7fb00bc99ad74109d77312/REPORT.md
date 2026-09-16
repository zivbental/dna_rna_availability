# YLR089C
Status: ok. Length: 2144 nt. Measured usable bases: 1122. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1122 | 0.3128 | 0.2865 |
| rnafold | ok | 1122 | 0.2298 | 0.2172 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 286 | 0.2411 | 0.2221 |
| seed_p | 286 | -0.1242 | -0.0653 |
| seed_p_vs_seed_pars | 233 | -0.2160 | -0.1496 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
