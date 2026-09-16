# YNL069C
Status: ok. Length: 735 nt. Measured usable bases: 586. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 586 | 0.2393 | 0.2295 |
| rnafold | ok | 586 | 0.2087 | 0.1958 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 497 | 0.0543 | 0.0295 |
| seed_p | 497 | -0.2680 | -0.1403 |
| seed_p_vs_seed_pars | 443 | -0.3061 | -0.1834 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
