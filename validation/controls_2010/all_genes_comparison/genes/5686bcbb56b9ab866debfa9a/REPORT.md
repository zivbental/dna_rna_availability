# YIL069C
Status: ok. Length: 637 nt. Measured usable bases: 264. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 264 | 0.3296 | 0.3113 |
| rnafold | ok | 264 | 0.3548 | 0.3463 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 190 | -0.0898 | -0.0435 |
| seed_p | 190 | -0.3965 | -0.4430 |
| seed_p_vs_seed_pars | 174 | -0.4022 | -0.4302 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
