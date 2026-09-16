# YGL076C
Status: ok. Length: 847 nt. Measured usable bases: 301. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 301 | 0.4317 | 0.4001 |
| rnafold | ok | 301 | 0.3354 | 0.3250 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 207 | -0.0907 | -0.4329 |
| seed_p | 207 | -0.0153 | -0.1553 |
| seed_p_vs_seed_pars | 183 | 0.0827 | -0.1070 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
