# YDR381W
Status: ok. Length: 958 nt. Measured usable bases: 762. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 762 | 0.4302 | 0.4349 |
| rnafold | ok | 762 | 0.4006 | 0.4174 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 652 | -0.2071 | -0.3250 |
| seed_p | 652 | -0.2501 | -0.2521 |
| seed_p_vs_seed_pars | 574 | -0.3915 | -0.3855 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
