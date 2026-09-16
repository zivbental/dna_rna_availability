# YFR004W
Status: ok. Length: 1017 nt. Measured usable bases: 589. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 589 | 0.3228 | 0.3169 |
| rnafold | ok | 589 | 0.2844 | 0.2775 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 258 | -0.2186 | -0.1937 |
| seed_p | 258 | 0.0180 | 0.0055 |
| seed_p_vs_seed_pars | 188 | 0.1371 | 0.0966 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
