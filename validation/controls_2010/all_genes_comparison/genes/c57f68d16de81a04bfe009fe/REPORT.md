# YLR287C-A
Status: ok. Length: 397 nt. Measured usable bases: 261. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 261 | 0.4336 | 0.4475 |
| rnafold | ok | 261 | 0.3377 | 0.3520 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 202 | -0.1609 | -0.3369 |
| seed_p | 202 | -0.4587 | -0.5398 |
| seed_p_vs_seed_pars | 188 | -0.5750 | -0.6167 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
