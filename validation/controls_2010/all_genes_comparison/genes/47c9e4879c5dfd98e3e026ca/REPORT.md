# YBL027W
Status: ok. Length: 684 nt. Measured usable bases: 372. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 372 | 0.3500 | 0.3721 |
| rnafold | ok | 372 | 0.2355 | 0.2665 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 247 | -0.1259 | -0.3607 |
| seed_p | 247 | 0.0432 | -0.1039 |
| seed_p_vs_seed_pars | 210 | -0.0604 | -0.0821 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
