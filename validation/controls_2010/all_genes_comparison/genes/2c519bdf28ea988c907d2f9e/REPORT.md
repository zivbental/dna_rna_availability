# YPR028W
Status: ok. Length: 739 nt. Measured usable bases: 562. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 562 | 0.2839 | 0.2866 |
| rnafold | ok | 562 | 0.2238 | 0.2418 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 467 | -0.2867 | -0.0821 |
| seed_p | 467 | -0.2435 | -0.1025 |
| seed_p_vs_seed_pars | 412 | -0.2559 | -0.0947 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
