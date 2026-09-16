# YDL174C
Status: ok. Length: 1892 nt. Measured usable bases: 991. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 991 | 0.3331 | 0.3082 |
| rnafold | ok | 991 | 0.3176 | 0.2883 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 251 | -0.2223 | -0.2359 |
| seed_p | 251 | -0.1030 | -0.0659 |
| seed_p_vs_seed_pars | 218 | 0.0100 | -0.0794 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
