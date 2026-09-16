# YGL048C
Status: ok. Length: 1308 nt. Measured usable bases: 1058. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1058 | 0.3845 | 0.3676 |
| rnafold | ok | 1058 | 0.3108 | 0.2982 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 857 | -0.2776 | -0.2266 |
| seed_p | 857 | -0.4773 | -0.4874 |
| seed_p_vs_seed_pars | 721 | -0.4694 | -0.4618 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
