# YIL111W
Status: ok. Length: 512 nt. Measured usable bases: 323. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 323 | 0.1069 | 0.1035 |
| rnafold | ok | 323 | 0.0349 | 0.0385 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 171 | -0.3143 | -0.3024 |
| seed_p | 171 | -0.0817 | -0.1911 |
| seed_p_vs_seed_pars | 105 | -0.1098 | -0.0634 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
