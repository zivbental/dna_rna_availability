# YMR225C
Status: ok. Length: 439 nt. Measured usable bases: 183. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 183 | 0.3090 | 0.2937 |
| rnafold | ok | 183 | 0.2996 | 0.2932 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 4 | undefined | undefined |
| seed_p | 4 | undefined | undefined |
| seed_p_vs_seed_pars | 4 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
