# YKL182W
Status: ok. Length: 6564 nt. Measured usable bases: 5190. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 5190 | 0.2866 | 0.2715 |
| rnafold | ok | 5190 | 0.2099 | 0.2009 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 4211 | -0.0308 | -0.0438 |
| seed_p | 4211 | -0.1191 | -0.1179 |
| seed_p_vs_seed_pars | 3444 | -0.1775 | -0.1981 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
