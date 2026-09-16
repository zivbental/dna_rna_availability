# YEL038W
Status: ok. Length: 765 nt. Measured usable bases: 590. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 590 | 0.2664 | 0.2387 |
| rnafold | ok | 590 | 0.1841 | 0.1675 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 447 | -0.2324 | -0.2326 |
| seed_p | 447 | 0.0145 | -0.0303 |
| seed_p_vs_seed_pars | 375 | -0.0947 | -0.1579 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
