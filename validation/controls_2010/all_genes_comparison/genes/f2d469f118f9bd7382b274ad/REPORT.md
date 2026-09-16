# YDR300C
Status: ok. Length: 1537 nt. Measured usable bases: 830. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 830 | 0.3742 | 0.3636 |
| rnafold | ok | 830 | 0.3414 | 0.3269 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 173 | -0.2308 | -0.4467 |
| seed_p | 173 | -0.2914 | -0.2672 |
| seed_p_vs_seed_pars | 111 | -0.4915 | -0.5996 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
