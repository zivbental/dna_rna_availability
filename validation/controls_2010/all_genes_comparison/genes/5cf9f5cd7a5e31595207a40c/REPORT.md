# YHR039C-A
Status: ok. Length: 415 nt. Measured usable bases: 306. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 306 | 0.3630 | 0.3900 |
| rnafold | ok | 306 | 0.2711 | 0.3305 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 205 | -0.2999 | -0.3604 |
| seed_p | 205 | -0.2649 | -0.2825 |
| seed_p_vs_seed_pars | 188 | -0.3366 | -0.3686 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
