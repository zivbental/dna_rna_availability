# YIL009C-A
Status: ok. Length: 704 nt. Measured usable bases: 366. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 366 | 0.2752 | 0.2571 |
| rnafold | ok | 366 | 0.2114 | 0.1963 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 205 | -0.5748 | -0.2902 |
| seed_p | 205 | -0.1326 | -0.2559 |
| seed_p_vs_seed_pars | 139 | -0.2929 | -0.3314 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
