# YKR094C
Status: ok. Length: 557 nt. Measured usable bases: 275. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 275 | 0.2885 | 0.2956 |
| rnafold | ok | 275 | 0.2758 | 0.2784 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 190 | 0.1448 | 0.1416 |
| seed_p | 190 | 0.0357 | 0.0304 |
| seed_p_vs_seed_pars | 166 | 0.0048 | 0.0723 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
