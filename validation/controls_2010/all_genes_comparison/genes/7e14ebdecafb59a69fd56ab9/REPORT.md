# YIL148W
Status: ok. Length: 467 nt. Measured usable bases: 199. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 199 | 0.2836 | 0.2903 |
| rnafold | ok | 199 | 0.2541 | 0.2040 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 125 | -0.1824 | -0.3747 |
| seed_p | 125 | -0.2598 | -0.3030 |
| seed_p_vs_seed_pars | 117 | 0.0338 | 0.1217 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
