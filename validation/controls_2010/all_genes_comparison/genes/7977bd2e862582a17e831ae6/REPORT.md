# YDR367W
Status: ok. Length: 785 nt. Measured usable bases: 484. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 484 | 0.2367 | 0.2370 |
| rnafold | ok | 484 | 0.1684 | 0.2007 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 276 | 0.0473 | 0.1303 |
| seed_p | 276 | -0.1728 | -0.0591 |
| seed_p_vs_seed_pars | 179 | -0.1129 | -0.0736 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
