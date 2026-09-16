# YEL021W
Status: ok. Length: 804 nt. Measured usable bases: 470. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 470 | 0.2862 | 0.2808 |
| rnafold | ok | 470 | 0.2332 | 0.2094 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 218 | -0.1911 | -0.2344 |
| seed_p | 218 | -0.1504 | -0.0932 |
| seed_p_vs_seed_pars | 182 | -0.2128 | -0.0763 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
