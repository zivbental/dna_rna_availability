# YGL234W
Status: ok. Length: 2553 nt. Measured usable bases: 2173. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2173 | 0.3333 | 0.3158 |
| rnafold | ok | 2173 | 0.2743 | 0.2680 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2001 | 0.0898 | -0.1120 |
| seed_p | 2001 | -0.1628 | -0.1889 |
| seed_p_vs_seed_pars | 1752 | -0.2071 | -0.2326 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
