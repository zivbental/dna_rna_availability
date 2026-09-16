# YOR307C
Status: ok. Length: 1639 nt. Measured usable bases: 841. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 841 | 0.3513 | 0.3422 |
| rnafold | ok | 841 | 0.2879 | 0.2934 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 188 | -0.6038 | -0.6831 |
| seed_p | 188 | -0.6327 | -0.6199 |
| seed_p_vs_seed_pars | 119 | -0.6599 | -0.6042 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
