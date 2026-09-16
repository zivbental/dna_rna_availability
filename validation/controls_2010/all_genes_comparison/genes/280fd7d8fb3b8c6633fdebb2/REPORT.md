# YOR241W
Status: ok. Length: 1714 nt. Measured usable bases: 860. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 860 | 0.2945 | 0.2902 |
| rnafold | ok | 860 | 0.2776 | 0.2886 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 160 | 0.0063 | -0.0588 |
| seed_p | 160 | -0.1370 | -0.0607 |
| seed_p_vs_seed_pars | 119 | -0.4840 | -0.3950 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
