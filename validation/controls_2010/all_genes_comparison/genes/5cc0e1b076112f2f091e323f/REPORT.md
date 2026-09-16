# YPL111W
Status: ok. Length: 1143 nt. Measured usable bases: 846. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 846 | 0.3038 | 0.3001 |
| rnafold | ok | 846 | 0.2268 | 0.2383 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 621 | -0.2007 | 0.0844 |
| seed_p | 621 | -0.2253 | -0.1448 |
| seed_p_vs_seed_pars | 527 | -0.2270 | -0.2577 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
