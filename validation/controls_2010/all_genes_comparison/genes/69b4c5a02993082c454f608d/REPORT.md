# YLR406C
Status: ok. Length: 534 nt. Measured usable bases: 259. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 259 | 0.4083 | 0.4063 |
| rnafold | ok | 259 | 0.3697 | 0.3744 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 153 | -0.1774 | -0.0590 |
| seed_p | 153 | -0.4132 | -0.4275 |
| seed_p_vs_seed_pars | 142 | -0.4576 | -0.5127 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
