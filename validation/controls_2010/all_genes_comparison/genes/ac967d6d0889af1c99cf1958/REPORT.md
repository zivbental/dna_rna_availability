# YML085C
Status: ok. Length: 1524 nt. Measured usable bases: 1116. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1116 | 0.2920 | 0.2638 |
| rnafold | ok | 1116 | 0.2541 | 0.2273 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 813 | 0.0000 | -0.0581 |
| seed_p | 813 | -0.1832 | -0.0833 |
| seed_p_vs_seed_pars | 654 | -0.3173 | -0.1912 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
