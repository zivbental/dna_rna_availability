# YDL012C
Status: ok. Length: 467 nt. Measured usable bases: 290. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 290 | 0.2050 | 0.1948 |
| rnafold | ok | 290 | 0.2033 | 0.2043 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 108 | 0.0487 | -0.0787 |
| seed_p | 108 | -0.0680 | -0.2422 |
| seed_p_vs_seed_pars | 82 | -0.2256 | -0.3828 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
