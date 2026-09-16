# YLR439W
Status: ok. Length: 1150 nt. Measured usable bases: 467. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 467 | 0.2354 | 0.2060 |
| rnafold | ok | 467 | 0.2099 | 0.1783 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 20 | 0.1320 | 0.5266 |
| seed_p | 20 | 0.1804 | -0.0568 |
| seed_p_vs_seed_pars | 8 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
