# YBR111W-A
Status: ok. Length: 475 nt. Measured usable bases: 157. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 157 | 0.3495 | 0.3474 |
| rnafold | ok | 157 | 0.3372 | 0.3575 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 13 | undefined | undefined |
| seed_p | 13 | undefined | undefined |
| seed_p_vs_seed_pars | 9 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
