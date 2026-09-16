# YBL079W
Status: ok. Length: 4816 nt. Measured usable bases: 1821.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1821 | 0.2890 | 0.2827 |
| rnafold | ok | 1821 | 0.2476 | 0.2444 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 91 | 0.3785 | 0.3172 |
| seed_p | 91 | 0.2341 | 0.1706 |
| seed_p_vs_seed_pars | 72 | 0.3346 | 0.2233 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
