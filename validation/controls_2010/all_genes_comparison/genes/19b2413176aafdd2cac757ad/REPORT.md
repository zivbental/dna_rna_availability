# YJR143C
Status: ok. Length: 2463 nt. Measured usable bases: 1951. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1951 | 0.3337 | 0.3177 |
| rnafold | ok | 1951 | 0.2720 | 0.2721 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1666 | 0.0535 | 0.0220 |
| seed_p | 1666 | -0.0677 | -0.0670 |
| seed_p_vs_seed_pars | 1372 | -0.2786 | -0.2068 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
