# YKL006C-A
Status: ok. Length: 366 nt. Measured usable bases: 165. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 165 | 0.5131 | 0.4886 |
| rnafold | ok | 165 | 0.4067 | 0.4364 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 52 | -0.0379 | -0.1584 |
| seed_p | 52 | -0.2495 | -0.3115 |
| seed_p_vs_seed_pars | 41 | 0.3753 | 0.4338 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
