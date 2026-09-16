# YHR141C
Status: ok. Length: 398 nt. Measured usable bases: 123. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 123 | 0.5290 | 0.5187 |
| rnafold | ok | 123 | 0.4511 | 0.4814 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 68 | -0.6204 | -0.2219 |
| seed_p | 68 | -0.4186 | 0.3607 |
| seed_p_vs_seed_pars | 66 | -0.3942 | 0.0383 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
