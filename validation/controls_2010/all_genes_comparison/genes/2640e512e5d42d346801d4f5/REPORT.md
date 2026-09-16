# YBL050W
Status: ok. Length: 1017 nt. Measured usable bases: 609. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 609 | 0.4113 | 0.4152 |
| rnafold | ok | 609 | 0.3737 | 0.3774 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 247 | 0.0287 | 0.1213 |
| seed_p | 247 | 0.2383 | 0.1738 |
| seed_p_vs_seed_pars | 180 | 0.0906 | -0.0002 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
