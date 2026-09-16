# YNL147W
Status: ok. Length: 629 nt. Measured usable bases: 218. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 218 | 0.2650 | 0.2405 |
| rnafold | ok | 218 | 0.2923 | 0.2538 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 26 | 0.1118 | -0.5065 |
| seed_p | 26 | -0.7529 | -0.6908 |
| seed_p_vs_seed_pars | 18 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
