# YNL231C
Status: ok. Length: 1374 nt. Measured usable bases: 563. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 563 | 0.2232 | 0.2354 |
| rnafold | ok | 563 | 0.1499 | 0.1798 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 123 | 0.0120 | -0.1321 |
| seed_p | 123 | -0.0616 | -0.0232 |
| seed_p_vs_seed_pars | 98 | -0.4538 | -0.5444 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
