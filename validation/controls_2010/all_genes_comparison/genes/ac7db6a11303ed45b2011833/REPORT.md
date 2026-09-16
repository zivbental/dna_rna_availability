# YDL125C
Status: ok. Length: 801 nt. Measured usable bases: 596. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 596 | 0.3396 | 0.3359 |
| rnafold | ok | 596 | 0.2816 | 0.2861 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 498 | -0.3418 | -0.4766 |
| seed_p | 498 | -0.3237 | -0.4200 |
| seed_p_vs_seed_pars | 417 | -0.4219 | -0.4352 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
