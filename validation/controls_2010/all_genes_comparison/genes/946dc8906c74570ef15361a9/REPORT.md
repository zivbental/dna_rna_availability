# YOL027C
Status: ok. Length: 1925 nt. Measured usable bases: 769. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 769 | 0.3453 | 0.3425 |
| rnafold | ok | 769 | 0.2897 | 0.2991 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | -0.5271 | -0.7965 |
| seed_p | 65 | -0.1145 | -0.1137 |
| seed_p_vs_seed_pars | 39 | -0.3362 | -0.4133 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
