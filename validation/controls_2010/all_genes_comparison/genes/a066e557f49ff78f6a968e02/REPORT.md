# YER056C-A
Status: ok. Length: 443 nt. Measured usable bases: 242. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 242 | 0.3302 | 0.3265 |
| rnafold | ok | 242 | 0.3134 | 0.3058 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 149 | 0.0258 | 0.2171 |
| seed_p | 149 | -0.3667 | -0.1536 |
| seed_p_vs_seed_pars | 124 | -0.6170 | -0.4455 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
