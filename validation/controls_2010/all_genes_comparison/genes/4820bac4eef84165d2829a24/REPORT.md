# YCL005W-A
Status: ok. Length: 326 nt. Measured usable bases: 240. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 240 | 0.1842 | 0.1642 |
| rnafold | ok | 240 | 0.1455 | 0.1336 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 216 | 0.1978 | -0.3003 |
| seed_p | 216 | -0.0856 | -0.1548 |
| seed_p_vs_seed_pars | 211 | -0.3537 | -0.2210 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
