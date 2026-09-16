# YBR082C
Status: ok. Length: 778 nt. Measured usable bases: 556. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 556 | 0.2058 | 0.1991 |
| rnafold | ok | 556 | 0.1125 | 0.1025 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 530 | -0.1951 | -0.2043 |
| seed_p | 530 | -0.2850 | -0.3145 |
| seed_p_vs_seed_pars | 448 | -0.3202 | -0.2320 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
