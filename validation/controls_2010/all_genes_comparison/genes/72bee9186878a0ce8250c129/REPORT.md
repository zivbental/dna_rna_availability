# YML035C
Status: ok. Length: 2594 nt. Measured usable bases: 1330. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1330 | 0.2929 | 0.2780 |
| rnafold | ok | 1330 | 0.2671 | 0.2568 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 275 | -0.0548 | -0.1887 |
| seed_p | 275 | -0.3962 | -0.2877 |
| seed_p_vs_seed_pars | 208 | -0.4627 | -0.2875 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
