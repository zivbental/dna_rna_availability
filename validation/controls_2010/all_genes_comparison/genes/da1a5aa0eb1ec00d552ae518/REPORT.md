# YKL180W
Status: ok. Length: 691 nt. Measured usable bases: 450. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 450 | 0.2920 | 0.2797 |
| rnafold | ok | 450 | 0.2637 | 0.2435 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 315 | -0.2533 | -0.1331 |
| seed_p | 315 | -0.1394 | -0.0455 |
| seed_p_vs_seed_pars | 280 | -0.2928 | -0.1938 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
