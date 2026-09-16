# YAL003W
Status: ok. Length: 844 nt. Measured usable bases: 765. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 765 | 0.3292 | 0.3370 |
| rnafold | ok | 765 | 0.2969 | 0.3011 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 736 | -0.0894 | -0.2878 |
| seed_p | 736 | -0.2250 | -0.2753 |
| seed_p_vs_seed_pars | 734 | -0.2305 | -0.3113 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
