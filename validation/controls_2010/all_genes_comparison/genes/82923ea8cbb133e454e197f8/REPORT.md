# YPR016C
Status: ok. Length: 923 nt. Measured usable bases: 766. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 766 | 0.2321 | 0.2254 |
| rnafold | ok | 766 | 0.2034 | 0.1918 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 691 | -0.0739 | 0.0025 |
| seed_p | 691 | -0.2704 | -0.1754 |
| seed_p_vs_seed_pars | 663 | -0.3294 | -0.2458 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
