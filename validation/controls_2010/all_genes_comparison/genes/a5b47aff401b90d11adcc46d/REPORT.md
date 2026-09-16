# YDR091C
Status: ok. Length: 2214 nt. Measured usable bases: 1691. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1691 | 0.2588 | 0.2347 |
| rnafold | ok | 1691 | 0.1794 | 0.1727 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1231 | 0.1007 | -0.0484 |
| seed_p | 1231 | -0.1181 | -0.1428 |
| seed_p_vs_seed_pars | 1017 | -0.2899 | -0.3021 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
