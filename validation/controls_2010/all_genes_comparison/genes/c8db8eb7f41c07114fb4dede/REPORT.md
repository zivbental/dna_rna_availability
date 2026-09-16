# YGR214W
Status: ok. Length: 840 nt. Measured usable bases: 557. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 557 | 0.3573 | 0.3769 |
| rnafold | ok | 557 | 0.2753 | 0.3062 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 332 | -0.3145 | -0.2859 |
| seed_p | 332 | -0.1878 | -0.1072 |
| seed_p_vs_seed_pars | 301 | -0.2109 | -0.2083 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
