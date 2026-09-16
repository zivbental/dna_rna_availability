# YJL079C
Status: ok. Length: 1249 nt. Measured usable bases: 851. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 851 | 0.2582 | 0.2365 |
| rnafold | ok | 851 | 0.2213 | 0.2156 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 496 | 0.1181 | -0.2061 |
| seed_p | 496 | -0.1693 | -0.3004 |
| seed_p_vs_seed_pars | 393 | -0.1740 | -0.1386 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
