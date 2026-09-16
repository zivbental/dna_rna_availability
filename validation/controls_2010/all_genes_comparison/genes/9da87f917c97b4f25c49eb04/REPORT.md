# YJL205C
Status: ok. Length: 309 nt. Measured usable bases: 150. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 150 | 0.4066 | 0.4008 |
| rnafold | ok | 150 | 0.3664 | 0.3735 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 52 | -0.4309 | -0.8698 |
| seed_p | 52 | -0.6452 | -0.8579 |
| seed_p_vs_seed_pars | 39 | -0.2550 | -0.4502 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
