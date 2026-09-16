# YOR234C
Status: ok. Length: 416 nt. Measured usable bases: 287. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 287 | 0.3888 | 0.3897 |
| rnafold | ok | 287 | 0.2670 | 0.2860 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 197 | -0.2764 | -0.3366 |
| seed_p | 197 | -0.3601 | -0.1783 |
| seed_p_vs_seed_pars | 177 | -0.2569 | -0.1224 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
