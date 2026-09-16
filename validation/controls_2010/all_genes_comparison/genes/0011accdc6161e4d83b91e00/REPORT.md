# YKL039W
Status: ok. Length: 1966 nt. Measured usable bases: 1143. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1143 | 0.2721 | 0.2478 |
| rnafold | ok | 1143 | 0.2269 | 0.2174 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 322 | 0.3967 | 0.2738 |
| seed_p | 322 | 0.1684 | 0.1364 |
| seed_p_vs_seed_pars | 233 | 0.0929 | 0.0987 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
