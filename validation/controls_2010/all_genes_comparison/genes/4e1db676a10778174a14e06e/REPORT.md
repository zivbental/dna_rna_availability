# YDL108W
Status: ok. Length: 1046 nt. Measured usable bases: 425. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 425 | 0.2164 | 0.2112 |
| rnafold | ok | 425 | 0.2431 | 0.2345 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 33 | 0.3145 | 0.3568 |
| seed_p | 33 | -0.6936 | -0.5061 |
| seed_p_vs_seed_pars | 31 | -0.6520 | -0.9305 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
