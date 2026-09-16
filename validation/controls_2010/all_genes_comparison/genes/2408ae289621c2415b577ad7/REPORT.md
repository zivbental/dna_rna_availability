# YPL179W
Status: ok. Length: 2042 nt. Measured usable bases: 976. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 976 | 0.2847 | 0.2693 |
| rnafold | ok | 976 | 0.2351 | 0.2209 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 233 | -0.1316 | -0.1387 |
| seed_p | 233 | -0.0404 | -0.0491 |
| seed_p_vs_seed_pars | 169 | -0.1110 | -0.1560 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
