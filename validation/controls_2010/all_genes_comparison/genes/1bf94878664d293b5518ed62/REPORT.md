# YLR315W
Status: ok. Length: 462 nt. Measured usable bases: 203. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 203 | 0.4709 | 0.4492 |
| rnafold | ok | 203 | 0.3825 | 0.3681 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 21 | -0.6764 | -0.8100 |
| seed_p | 21 | -0.0256 | 0.1766 |
| seed_p_vs_seed_pars | 4 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
