# YDR397C
Status: ok. Length: 573 nt. Measured usable bases: 291. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 291 | 0.4252 | 0.4422 |
| rnafold | ok | 291 | 0.4053 | 0.4317 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 69 | -0.4953 | -0.6809 |
| seed_p | 69 | -0.1904 | -0.1918 |
| seed_p_vs_seed_pars | 45 | -0.1678 | -0.1329 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
