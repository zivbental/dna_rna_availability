# YDL083C
Status: ok. Length: 550 nt. Measured usable bases: 338. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 338 | 0.3633 | 0.3795 |
| rnafold | ok | 338 | 0.2373 | 0.2800 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 168 | -0.4473 | -0.5752 |
| seed_p | 168 | -0.1703 | -0.1838 |
| seed_p_vs_seed_pars | 147 | -0.2000 | -0.1668 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
