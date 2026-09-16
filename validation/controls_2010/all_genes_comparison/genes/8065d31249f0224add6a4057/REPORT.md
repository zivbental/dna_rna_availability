# YPL249C-A
Status: ok. Length: 459 nt. Measured usable bases: 335. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 335 | 0.3804 | 0.3980 |
| rnafold | ok | 335 | 0.3073 | 0.3023 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 283 | -0.3574 | -0.4628 |
| seed_p | 283 | -0.4338 | -0.4182 |
| seed_p_vs_seed_pars | 256 | -0.2789 | -0.3024 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
