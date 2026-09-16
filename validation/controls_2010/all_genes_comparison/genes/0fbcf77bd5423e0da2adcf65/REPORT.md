# YPL057C
Status: ok. Length: 1677 nt. Measured usable bases: 755. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 755 | 0.2866 | 0.2728 |
| rnafold | ok | 755 | 0.2597 | 0.2782 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 103 | 0.2365 | 0.2858 |
| seed_p | 103 | -0.3615 | -0.2106 |
| seed_p_vs_seed_pars | 71 | -0.4225 | -0.0609 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
