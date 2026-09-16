# YKL002W
Status: ok. Length: 855 nt. Measured usable bases: 431. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 431 | 0.2738 | 0.2505 |
| rnafold | ok | 431 | 0.2328 | 0.2209 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 81 | -0.0405 | -0.2554 |
| seed_p | 81 | -0.2277 | -0.3233 |
| seed_p_vs_seed_pars | 62 | -0.2350 | -0.2236 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
