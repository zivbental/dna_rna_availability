# YPL143W
Status: ok. Length: 394 nt. Measured usable bases: 294. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 294 | 0.3088 | 0.3105 |
| rnafold | ok | 294 | 0.2747 | 0.3101 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 231 | 0.0892 | -0.3298 |
| seed_p | 231 | -0.1274 | -0.2210 |
| seed_p_vs_seed_pars | 204 | -0.1799 | -0.1271 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
