# YEL042W
Status: ok. Length: 1846 nt. Measured usable bases: 1421. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1421 | 0.2676 | 0.2543 |
| rnafold | ok | 1421 | 0.2462 | 0.2361 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1033 | -0.1884 | -0.1827 |
| seed_p | 1033 | -0.3186 | -0.2775 |
| seed_p_vs_seed_pars | 798 | -0.3179 | -0.2912 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
