# YDL136W
Status: ok. Length: 528 nt. Measured usable bases: 119. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 119 | 0.2616 | 0.2673 |
| rnafold | ok | 119 | 0.3011 | 0.2816 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 64 | -0.8428 | -0.4942 |
| seed_p | 64 | -0.5932 | -0.7630 |
| seed_p_vs_seed_pars | 62 | -0.2301 | -0.3344 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
