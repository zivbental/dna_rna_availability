# YMR194C-B
Status: ok. Length: 365 nt. Measured usable bases: 97. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 97 | 0.3301 | 0.3012 |
| rnafold | ok | 97 | 0.3345 | 0.3507 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 0 | undefined | undefined |
| seed_p | 0 | undefined | undefined |
| seed_p_vs_seed_pars | 0 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
