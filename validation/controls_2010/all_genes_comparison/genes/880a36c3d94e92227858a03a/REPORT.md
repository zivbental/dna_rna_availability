# YGL103W
Status: ok. Length: 554 nt. Measured usable bases: 511. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 511 | 0.4189 | 0.4184 |
| rnafold | ok | 511 | 0.3851 | 0.4045 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 490 | -0.1743 | -0.5389 |
| seed_p | 490 | -0.3112 | -0.4580 |
| seed_p_vs_seed_pars | 479 | -0.3003 | -0.5010 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
