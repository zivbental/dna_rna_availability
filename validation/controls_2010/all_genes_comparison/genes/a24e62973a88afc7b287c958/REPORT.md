# YML008C
Status: ok. Length: 1252 nt. Measured usable bases: 979. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 979 | 0.3552 | 0.3508 |
| rnafold | ok | 979 | 0.2469 | 0.2581 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 771 | -0.1058 | -0.0242 |
| seed_p | 771 | -0.1249 | -0.0739 |
| seed_p_vs_seed_pars | 627 | -0.3007 | -0.2351 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
