# YPL234C
Status: ok. Length: 663 nt. Measured usable bases: 530. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 530 | 0.2154 | 0.2342 |
| rnafold | ok | 530 | 0.2101 | 0.2460 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 494 | -0.0803 | -0.0831 |
| seed_p | 494 | -0.0533 | -0.0546 |
| seed_p_vs_seed_pars | 475 | -0.1217 | -0.0594 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
