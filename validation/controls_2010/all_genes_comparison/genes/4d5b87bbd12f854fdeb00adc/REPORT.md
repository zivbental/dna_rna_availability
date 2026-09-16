# YHR041C
Status: ok. Length: 855 nt. Measured usable bases: 534. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 534 | 0.1823 | 0.1692 |
| rnafold | ok | 534 | 0.1353 | 0.1394 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 429 | 0.1051 | 0.0207 |
| seed_p | 429 | -0.0810 | -0.0643 |
| seed_p_vs_seed_pars | 388 | -0.0771 | -0.0846 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
