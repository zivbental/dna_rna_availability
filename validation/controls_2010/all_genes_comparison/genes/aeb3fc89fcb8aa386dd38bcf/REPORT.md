# YDL045W-A
Status: ok. Length: 440 nt. Measured usable bases: 223. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 223 | 0.2483 | 0.2373 |
| rnafold | ok | 223 | 0.2128 | 0.2110 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 78 | -0.0272 | 0.0134 |
| seed_p | 78 | -0.1000 | -0.1316 |
| seed_p_vs_seed_pars | 37 | -0.6721 | -0.7905 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
