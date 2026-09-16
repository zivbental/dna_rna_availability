# YBR247C
Status: ok. Length: 1550 nt. Measured usable bases: 602. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 602 | 0.3546 | 0.3352 |
| rnafold | ok | 602 | 0.2689 | 0.2473 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 69 | -0.0333 | -0.2840 |
| seed_p | 69 | -0.0540 | -0.0265 |
| seed_p_vs_seed_pars | 52 | -0.5354 | -0.4596 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
