# YJL191W
Status: ok. Length: 540 nt. Measured usable bases: 296. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 296 | 0.2193 | 0.1937 |
| rnafold | ok | 296 | 0.1933 | 0.1751 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 176 | 0.0129 | 0.2492 |
| seed_p | 176 | 0.0538 | 0.2532 |
| seed_p_vs_seed_pars | 170 | 0.0594 | 0.2265 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
