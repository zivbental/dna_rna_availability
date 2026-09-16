# YBR278W
Status: ok. Length: 699 nt. Measured usable bases: 302. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 302 | 0.3997 | 0.3981 |
| rnafold | ok | 302 | 0.2710 | 0.2773 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | 0.4168 | 0.4295 |
| seed_p | 31 | -0.5800 | -0.2326 |
| seed_p_vs_seed_pars | 27 | -0.8772 | -0.4587 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
