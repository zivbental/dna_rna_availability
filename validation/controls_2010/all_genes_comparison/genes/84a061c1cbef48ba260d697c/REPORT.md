# YJR021C
Status: ok. Length: 1148 nt. Measured usable bases: 389. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 389 | 0.3359 | 0.3528 |
| rnafold | ok | 389 | 0.2732 | 0.2896 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | 0.1136 | -0.4546 |
| seed_p | 34 | 0.3091 | -0.0806 |
| seed_p_vs_seed_pars | 24 | 0.6908 | 0.4320 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
