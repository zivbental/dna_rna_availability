# YBR269C
Status: ok. Length: 549 nt. Measured usable bases: 317. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 317 | 0.4065 | 0.4028 |
| rnafold | ok | 317 | 0.2268 | 0.2151 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 128 | 0.0389 | -0.3348 |
| seed_p | 128 | -0.2672 | -0.3721 |
| seed_p_vs_seed_pars | 109 | -0.5000 | -0.5373 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
