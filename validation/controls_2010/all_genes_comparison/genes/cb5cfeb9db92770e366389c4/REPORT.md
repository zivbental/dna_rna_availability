# YER074W
Status: ok. Length: 540 nt. Measured usable bases: 192. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 192 | 0.3539 | 0.3524 |
| rnafold | ok | 192 | 0.2180 | 0.1840 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | -0.1427 | -0.0836 |
| seed_p | 118 | 0.0544 | 0.0580 |
| seed_p_vs_seed_pars | 88 | -0.0126 | 0.1946 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
