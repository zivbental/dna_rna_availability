# YMR071C
Status: ok. Length: 597 nt. Measured usable bases: 416. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 416 | 0.2991 | 0.2913 |
| rnafold | ok | 416 | 0.2208 | 0.2150 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 272 | 0.0151 | -0.1852 |
| seed_p | 272 | -0.1909 | -0.3066 |
| seed_p_vs_seed_pars | 258 | -0.2784 | -0.3634 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
