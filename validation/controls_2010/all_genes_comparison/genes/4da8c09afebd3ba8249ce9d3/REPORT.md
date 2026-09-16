# YLR333C
Status: ok. Length: 887 nt. Measured usable bases: 381. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 381 | 0.3184 | 0.3150 |
| rnafold | ok | 381 | 0.3212 | 0.3272 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 194 | -0.3442 | -0.3008 |
| seed_p | 194 | -0.5539 | -0.3429 |
| seed_p_vs_seed_pars | 171 | -0.6057 | -0.4944 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
