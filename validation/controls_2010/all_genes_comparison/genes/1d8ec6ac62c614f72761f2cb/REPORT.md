# YHR199C-A
Status: ok. Length: 222 nt. Measured usable bases: 106. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 106 | 0.4817 | 0.5049 |
| rnafold | ok | 106 | 0.5340 | 0.5482 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 9 | undefined | undefined |
| seed_p | 9 | undefined | undefined |
| seed_p_vs_seed_pars | 3 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
