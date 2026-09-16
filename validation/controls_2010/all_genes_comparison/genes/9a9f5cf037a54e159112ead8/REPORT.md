# YIL156W-B
Status: ok. Length: 314 nt. Measured usable bases: 65. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 65 | 0.3715 | 0.3011 |
| rnafold | ok | 65 | 0.3763 | 0.3059 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 32 | -0.8782 | -0.9080 |
| seed_p | 32 | -0.5736 | -0.5202 |
| seed_p_vs_seed_pars | 19 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
