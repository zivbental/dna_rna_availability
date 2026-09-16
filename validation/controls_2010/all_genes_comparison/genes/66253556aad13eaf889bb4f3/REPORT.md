# YIL018W
Status: ok. Length: 880 nt. Measured usable bases: 282. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 282 | 0.3453 | 0.3284 |
| rnafold | ok | 282 | 0.3211 | 0.3007 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 123 | -0.4766 | -0.4707 |
| seed_p | 123 | -0.4056 | -0.3037 |
| seed_p_vs_seed_pars | 107 | -0.5226 | -0.2555 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
