# YLR270W
Status: ok. Length: 1255 nt. Measured usable bases: 577. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 577 | 0.2246 | 0.2117 |
| rnafold | ok | 577 | 0.1678 | 0.1582 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 119 | -0.1120 | 0.0747 |
| seed_p | 119 | -0.0646 | 0.0033 |
| seed_p_vs_seed_pars | 78 | 0.1760 | 0.0004 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
