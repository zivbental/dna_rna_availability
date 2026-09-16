# YPL154C
Status: ok. Length: 1536 nt. Measured usable bases: 1242. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1242 | 0.3000 | 0.2963 |
| rnafold | ok | 1242 | 0.2687 | 0.2717 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1066 | -0.2387 | -0.1402 |
| seed_p | 1066 | -0.2140 | -0.1381 |
| seed_p_vs_seed_pars | 941 | -0.2438 | -0.2528 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
