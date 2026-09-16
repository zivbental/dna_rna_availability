# YJR094W-A
Status: ok. Length: 450 nt. Measured usable bases: 350. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 350 | 0.4067 | 0.4037 |
| rnafold | ok | 350 | 0.4115 | 0.3991 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 291 | -0.3068 | -0.3831 |
| seed_p | 291 | -0.4647 | -0.4612 |
| seed_p_vs_seed_pars | 282 | -0.5003 | -0.4684 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
