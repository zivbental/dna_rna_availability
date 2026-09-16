# YPL241C
Status: ok. Length: 875 nt. Measured usable bases: 320. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 320 | 0.2963 | 0.2766 |
| rnafold | ok | 320 | 0.2078 | 0.2032 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | 0.1840 | 0.3272 |
| seed_p | 77 | 0.5603 | 0.5571 |
| seed_p_vs_seed_pars | 60 | 0.5343 | 0.5822 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
