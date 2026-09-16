# YLR199C
Status: ok. Length: 1032 nt. Measured usable bases: 472. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 472 | 0.2511 | 0.2571 |
| rnafold | ok | 472 | 0.2291 | 0.2322 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 108 | 0.1006 | -0.2783 |
| seed_p | 108 | 0.3364 | 0.1290 |
| seed_p_vs_seed_pars | 90 | -0.0926 | -0.0528 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
