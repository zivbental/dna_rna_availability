# RDN37-1
Status: ok. Length: 5354 nt. Measured usable bases: 5261. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 5261 | 0.4360 | 0.4192 |
| rnafold | ok | 5261 | 0.3735 | 0.3695 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 5233 | 0.0166 | -0.1360 |
| seed_p | 5233 | -0.1242 | -0.1369 |
| seed_p_vs_seed_pars | 5215 | -0.3135 | -0.2677 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
