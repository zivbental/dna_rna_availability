# YCR028C-A
Status: ok. Length: 632 nt. Measured usable bases: 472. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 472 | 0.3996 | 0.3673 |
| rnafold | ok | 472 | 0.4269 | 0.3958 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 372 | -0.4372 | -0.2336 |
| seed_p | 372 | -0.3190 | -0.1536 |
| seed_p_vs_seed_pars | 314 | -0.4319 | -0.2738 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
