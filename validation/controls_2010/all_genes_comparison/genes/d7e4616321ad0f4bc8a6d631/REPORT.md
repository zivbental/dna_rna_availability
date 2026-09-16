# YCL012C
Status: ok. Length: 585 nt. Measured usable bases: 184. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 184 | 0.4397 | 0.3865 |
| rnafold | ok | 184 | 0.2991 | 0.2593 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 5 | undefined | undefined |
| seed_p | 5 | undefined | undefined |
| seed_p_vs_seed_pars | 5 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
