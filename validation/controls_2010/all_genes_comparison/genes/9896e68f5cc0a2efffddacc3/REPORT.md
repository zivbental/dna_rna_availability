# YLR390W-A
Status: ok. Length: 978 nt. Measured usable bases: 726. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 726 | 0.1915 | 0.1747 |
| rnafold | ok | 726 | 0.1191 | 0.1201 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 524 | -0.1627 | -0.0940 |
| seed_p | 524 | -0.1685 | -0.1339 |
| seed_p_vs_seed_pars | 472 | -0.1846 | -0.1327 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
