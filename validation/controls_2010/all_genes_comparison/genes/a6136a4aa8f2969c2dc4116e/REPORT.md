# YBL018C
Status: ok. Length: 468 nt. Measured usable bases: 258. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 258 | 0.4269 | 0.4317 |
| rnafold | ok | 258 | 0.3990 | 0.4318 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 84 | 0.1105 | -0.2819 |
| seed_p | 84 | 0.1609 | 0.0646 |
| seed_p_vs_seed_pars | 39 | -0.2502 | -0.2889 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
