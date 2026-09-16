# YDL130W
Status: ok. Length: 433 nt. Measured usable bases: 336. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 336 | 0.3255 | 0.3281 |
| rnafold | ok | 336 | 0.3119 | 0.3212 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 293 | -0.2816 | -0.4794 |
| seed_p | 293 | -0.2482 | -0.2230 |
| seed_p_vs_seed_pars | 252 | -0.1614 | -0.1576 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
