# YNL078W
Status: ok. Length: 1402 nt. Measured usable bases: 801. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 801 | 0.3280 | 0.3112 |
| rnafold | ok | 801 | 0.2344 | 0.2401 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 277 | -0.4921 | -0.5491 |
| seed_p | 277 | -0.4841 | -0.3837 |
| seed_p_vs_seed_pars | 201 | -0.6429 | -0.4482 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
