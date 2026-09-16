# YDR447C
Status: ok. Length: 526 nt. Measured usable bases: 257. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 257 | 0.3096 | 0.3105 |
| rnafold | ok | 257 | 0.2526 | 0.2667 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 130 | 0.0278 | -0.1072 |
| seed_p | 130 | 0.3492 | 0.2408 |
| seed_p_vs_seed_pars | 124 | 0.1907 | -0.0196 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
