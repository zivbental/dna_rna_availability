# YER074W-A
Status: ok. Length: 347 nt. Measured usable bases: 231. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 231 | 0.3094 | 0.3033 |
| rnafold | ok | 231 | 0.2841 | 0.2715 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 139 | -0.1571 | -0.0863 |
| seed_p | 139 | -0.1844 | -0.2369 |
| seed_p_vs_seed_pars | 104 | -0.4179 | -0.5014 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
