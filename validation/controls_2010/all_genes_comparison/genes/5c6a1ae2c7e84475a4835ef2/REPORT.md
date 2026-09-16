# YNL096C
Status: ok. Length: 784 nt. Measured usable bases: 514. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 514 | 0.3618 | 0.3492 |
| rnafold | ok | 514 | 0.3348 | 0.3180 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 390 | -0.3229 | -0.3087 |
| seed_p | 390 | -0.1490 | -0.1912 |
| seed_p_vs_seed_pars | 354 | -0.3030 | -0.2578 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
